text="Hello there! I'm learning Python for NLP. It's exciting, isn't it?"
text=text.lower()
c='!'
text=text.replace(c,"")
c="'"
text=text.replace(c,"")
c="'"
text=text.replace(c,"")
c='.'
text=text.replace(c,"")
c="?"
text=text.replace(c,"")
c=","
text=text.replace(c,"")
text=text.split()
len(text)
text[4]="Natural Language Procesing"

print(text)