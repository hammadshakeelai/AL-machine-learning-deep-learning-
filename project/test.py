import os
# ─── Redirect caches to D: ───────────────────────────────────────────────────────
os.environ["HF_HOME"]        = r"D:\huggingface_cache"
os.environ["XDG_CACHE_HOME"] = r"D:\huggingface_cache"
# Suppress protobuf & TF® warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import re, emoji, torch, warnings
import chromadb, gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

warnings.filterwarnings("ignore", ".*Protobuf.*")

# ─── 1) Pure-PyTorch Embedder ───────────────────────────────────────────────────
class PTEmbedder:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model     = AutoModelForCausalLM.from_pretrained(
            model_name.replace("sentence-transformers/", ""),
            torch_dtype=torch.float32
        ).eval().to(self._device())

    def _device(self):
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def encode(self, texts):
        inputs = self.tokenizer(
            texts, padding=True, truncation=True, return_tensors="pt"
        ).to(self._device())
        with torch.no_grad():
            out = self.model.model(**inputs, return_dict=True)
        hidden = out.last_hidden_state
        mask   = inputs.attention_mask.unsqueeze(-1)
        summed = (hidden * mask).sum(dim=1)
        counts = mask.sum(dim=1).clamp(min=1)
        return (summed / counts).cpu().numpy()

# ─── 2) Style & Sentiment Analyzer ─────────────────────────────────────────────
class StyleSentimentAnalyzer:
    def __init__(self):
        self.vader  = SentimentIntensityAnalyzer()
        self.slang  = {"gonna","wanna","lol","omg",
                      "dunno","brb","idk","btw",
                      "fuck","ur","ur","cuz",
                      "b4","lmao","smh","tbh",
                      "bitch","thx","pls","plz",
                      "kinda","sorta","gimme",
                      "lemme","gotta","cya","hmu",
                      "bff","imo","fyi","tbh",
                      "lmk","wut","wtf","yolo",
                      "bday","bffl","tbh","idc",
                      "smh","fml","tbh","btw","imo"}
        self.em_pat = re.compile("[\U0001F600-\U0001F64F]+", flags=re.UNICODE)

    def analyze(self, text: str):
        low      = text.lower()
        informal = any(tok in low for tok in self.slang)
        has_emoji= bool(self.em_pat.search(text))
        length   = len(text.split())
        score    = self.vader.polarity_scores(text)["compound"]
        if score >= 0.05:   label = "positive"
        elif score <= -0.05: label = "negative"
        else:                label = "neutral"
        return {
            "formality":       "Informal" if (informal or has_emoji) else "Formal",
            "emoji":           has_emoji,
            "sentence_length": length,
            "sentiment_label": label,
            "sentiment_score": score
        }

# ─── 3) Adaptive Chatbot with CPU Offload ───────────────────────────────────────
class AdaptiveChatbot:
    def __init__(self):
        model_id   = "tiiuae/falcon-7b"
        offload_dir= r"D:\huggingface_offload"
        os.makedirs(offload_dir, exist_ok=True)

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)

        # Load base Falcon-7B with CPU offload
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            offload_folder=offload_dir,
            offload_state_dict=True,
            torch_dtype=(torch.float16 if torch.cuda.is_available() else torch.float32),
        )

        # Generation pipeline
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=150,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )

        # Embedder, analyzer, and memory
        self.embedder = PTEmbedder()
        self.analyzer = StyleSentimentAnalyzer()
        self.client   = chromadb.Client()
        self.col      = self.client.get_or_create_collection("chat_memory")

    def store(self, speaker: str, text: str):
        emb  = self.embedder.encode([text])[0].tolist()
        meta = {"speaker": speaker}
        if speaker == "user":
            meta.update(self.analyzer.analyze(text))
        idx  = len(self.col.get()["ids"])
        self.col.add(
            documents=[text],
            embeddings=[emb],
            metadatas=[meta],
            ids=[f"id_{idx}"]
        )

    def context(self, turns: int = 3) -> str:
        docs = self.col.get()
        seq  = list(zip(docs["documents"], docs["metadatas"]))[-(turns*2):]
        return "\n".join(
            f"{'User' if m['speaker']=='user' else 'AI'}: {t}"
            for t,m in seq
        )

    def reply(self, user_msg: str) -> str:
        self.store("user", user_msg)
        prompt = f"{self.context()}\nUser: {user_msg}\nAI:"
        out    = self.generator(prompt)[0]["generated_text"]
        ans    = out.split("AI:")[-1].strip()
        self.store("ai", ans)
        return ans

# ─── 4) Gradio UI ───────────────────────────────────────────────────────────────
bot = AdaptiveChatbot()

def respond(msg, history):
    reply = bot.reply(msg)
    history.append((msg, reply))
    return history

with gr.Blocks() as demo:
    gr.Markdown("## 🎯 Falcon-7B Base Chatbot (CPU-Offloaded)")
    chat_ui = gr.Chatbot()
    user_in = gr.Textbox(placeholder="Type your message…", label="You")
    user_in.submit(respond, [user_in, chat_ui], chat_ui)
    demo.launch()
