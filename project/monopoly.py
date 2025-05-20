import tkinter as tk
from tkinter import messagebox, simpledialog
import random

BOARD_SIZE = 600
SPACE_SIZE = 60
PLAYER_COLORS = ["red", "blue", "green", "orange"]
PROPERTY_COLORS = {
    "brown": "#8B4513",
    "lightblue": "#ADD8E6",
    "pink": "#FF69B4",
    "orange": "#FFA500",
    "red": "#FF0000",
    "yellow": "#FFFF00",
    "green": "#008000",
    "blue": "#0000FF"
}

PROPERTY_NAMES = [
    "Go", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax", "Reading RR", "Oriental Ave", "Chance", "Vermont Ave", "Connecticut Ave", "Jail",
    "St. Charles Pl", "Electric Co", "States Ave", "Virginia Ave", "Pennsylvania RR", "St. James Pl", "Community Chest", "Tennessee Ave", "New York Ave", "Free Parking",
    "Kentucky Ave", "Chance", "Indiana Ave", "Illinois Ave", "B&O RR", "Atlantic Ave", "Ventnor Ave", "Water Works", "Marvin Gardens", "Go To Jail",
    "Pacific Ave", "North Carolina Ave", "Community Chest", "Pennsylvania Ave", "Short Line RR", "Chance", "Park Place", "Luxury Tax", "Boardwalk"
]

PROPERTY_TYPES = [
    "special", "brown", "special", "brown", "tax", "rr", "lightblue", "special", "lightblue", "lightblue", "jail",
    "pink", "utility", "pink", "pink", "rr", "orange", "special", "orange", "orange", "special",
    "red", "special", "red", "red", "rr", "yellow", "yellow", "utility", "yellow", "gotojail",
    "green", "green", "special", "green", "rr", "special", "blue", "tax", "blue"
]

PROPERTY_SETS = {
    "brown": [1, 3],
    "lightblue": [6, 8, 9],
    "pink": [11, 13, 14],
    "orange": [16, 18, 19],
    "red": [21, 23, 24],
    "yellow": [26, 27, 29],
    "green": [31, 32, 34],
    "blue": [37, 39]
}

TAX_AMOUNTS = {4: 200, 38: 100}  # Income Tax, Luxury Tax
JAIL_POS = 10
GOTO_JAIL_POS = 30
NUM_SPACES = len(PROPERTY_NAMES)

class Player:
    def __init__(self, name, color, idx):
        self.name = name
        self.color = color
        self.position = 0
        self.money = 1500
        self.idx = idx
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.has_rolled = False

class MonopolyGUI:
    def __init__(self, root, num_players=2):
        self.root = root
        self.root.title("Monopoly Board")
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}", PLAYER_COLORS[i], i) for i in range(num_players)]
        self.current_player = 0
        self.dice_value = 0
        self.owners = [None] * NUM_SPACES
        self.can_roll = True
        self.setup_gui()

    def setup_gui(self):
        self.canvas = tk.Canvas(self.root, width=BOARD_SIZE, height=BOARD_SIZE, bg="white")
        self.canvas.grid(row=0, column=0, rowspan=20)
        self.draw_board()
        self.info_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.info_label.grid(row=0, column=1, sticky="w")
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=1, column=1, sticky="w")
        self.end_turn_button = tk.Button(self.root, text="End Turn", command=self.end_turn)
        self.end_turn_button.grid(row=2, column=1, sticky="w")
        self.buy_button = tk.Button(self.root, text="Buy Property", command=self.buy_property)
        self.buy_button.grid(row=3, column=1, sticky="w")
        self.update_info()
        self.draw_tokens()

    def draw_board(self):
        self.space_coords = []
        n = 10
        # Bottom row (0-10)
        for i in range(n+1):
            x1 = BOARD_SIZE - (i+1)*SPACE_SIZE
            y1 = BOARD_SIZE - SPACE_SIZE
            x2 = BOARD_SIZE - i*SPACE_SIZE
            y2 = BOARD_SIZE
            self.space_coords.append((x1, y1, x2, y2))
        # Left column (11-20)
        for i in range(1, n+1):
            x1 = 0
            y1 = BOARD_SIZE - (i+1)*SPACE_SIZE
            x2 = SPACE_SIZE
            y2 = BOARD_SIZE - i*SPACE_SIZE
            self.space_coords.append((x1, y1, x2, y2))
        # Top row (21-30)
        for i in range(1, n+1):
            x1 = (i-1)*SPACE_SIZE
            y1 = 0
            x2 = i*SPACE_SIZE
            y2 = SPACE_SIZE
            self.space_coords.append((x1, y1, x2, y2))
        # Right column (31-39)
        for i in range(1, n):
            x1 = BOARD_SIZE - SPACE_SIZE
            y1 = i*SPACE_SIZE
            x2 = BOARD_SIZE
            y2 = (i+1)*SPACE_SIZE
            self.space_coords.append((x1, y1, x2, y2))
        # Draw spaces
        for i, (x1, y1, x2, y2) in enumerate(self.space_coords):
            color = PROPERTY_COLORS.get(PROPERTY_TYPES[i], "white") if PROPERTY_TYPES[i] not in ["special", "tax", "rr", "utility", "jail", "gotojail"] else "#eee"
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=2)
            name = PROPERTY_NAMES[i]
            self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text=name, font=("Arial", 7), width=SPACE_SIZE-4)

    def draw_tokens(self):
        # Remove old tokens
        self.canvas.delete("token")
        for player in self.players:
            x1, y1, x2, y2 = self.space_coords[player.position]
            # Offset tokens so they don't overlap
            offset = player.idx * 10
            cx = (x1 + x2)//2 + offset - 10
            cy = (y1 + y2)//2 + offset - 10
            self.canvas.create_oval(cx-10, cy-10, cx+10, cy+10, fill=player.color, tags="token")

    def update_info(self):
        p = self.players[self.current_player]
        jail_status = " (In Jail: {} turns left)".format(3 - p.jail_turns) if p.in_jail else ""
        self.info_label.config(text=f"{p.name} | Money: ${p.money} | Position: {PROPERTY_NAMES[p.position]}{jail_status}")
        # Enable/disable roll button based on can_roll and jail
        if self.can_roll and not p.in_jail:
            self.roll_button.config(state=tk.NORMAL)
        else:
            self.roll_button.config(state=tk.DISABLED)
        # End turn only if player has rolled or is in jail
        if p.has_rolled or p.in_jail:
            self.end_turn_button.config(state=tk.NORMAL)
        else:
            self.end_turn_button.config(state=tk.DISABLED)

    def roll_dice(self):
        p = self.players[self.current_player]
        if p.in_jail:
            p.jail_turns += 1
            if p.jail_turns >= 3:
                p.in_jail = False
                p.jail_turns = 0
                messagebox.showinfo("Jail", f"{p.name} is released from jail!")
            else:
                messagebox.showinfo("Jail", f"{p.name} is in jail. Turns left: {3 - p.jail_turns}")
            self.can_roll = False
            p.has_rolled = True
            self.update_info()
            return
        dice = random.randint(1, 6)
        self.dice_value = dice
        messagebox.showinfo("Dice Roll", f"{p.name} rolled a {dice}!")
        old_pos = p.position
        p.position = (p.position + dice) % NUM_SPACES
        self.draw_tokens()
        self.handle_landing(p)
        if dice == 6:
            self.can_roll = True
            messagebox.showinfo("Extra Turn", f"{p.name} rolled a 6 and gets another roll!")
        else:
            self.can_roll = False
        p.has_rolled = True
        self.update_info()

    def handle_landing(self, p):
        pos = p.position
        t = PROPERTY_TYPES[pos]
        # Go to Jail
        if t == "gotojail":
            messagebox.showinfo("Go To Jail", f"{p.name} goes to Jail!")
            p.position = JAIL_POS
            p.in_jail = True
            p.jail_turns = 0
            self.draw_tokens()
            return
        # Tax
        if t == "tax":
            tax = TAX_AMOUNTS.get(pos, 100)
            p.money -= tax
            messagebox.showinfo("Tax", f"{p.name} paid ${tax} in taxes!")
        # Rent
        if self.owners[pos] is not None and self.owners[pos] != self.current_player:
            owner = self.players[self.owners[pos]]
            rent = self.calculate_rent(pos, owner)
            p.money -= rent
            owner.money += rent
            messagebox.showinfo("Rent", f"{p.name} paid ${rent} rent to {owner.name}!")

    def calculate_rent(self, pos, owner):
        # Double rent if owner has full set
        t = PROPERTY_TYPES[pos]
        base_rent = 50  # Demo value
        for color, idxs in PROPERTY_SETS.items():
            if pos in idxs:
                if all(self.owners[i] == self.owners[pos] for i in idxs):
                    return base_rent * 2
        return base_rent

    def end_turn(self):
        p = self.players[self.current_player]
        p.has_rolled = False
        self.current_player = (self.current_player + 1) % self.num_players
        self.can_roll = True
        self.update_info()

    def buy_property(self):
        p = self.players[self.current_player]
        pos = p.position
        t = PROPERTY_TYPES[pos]
        if t not in PROPERTY_SETS:
            messagebox.showinfo("Buy Property", "This is not a property!")
            return
        if self.owners[pos] is not None:
            messagebox.showinfo("Buy Property", "Already owned!")
            return
        price = 100  # For demo, all properties cost 100
        if p.money >= price:
            p.money -= price
            self.owners[pos] = self.current_player
            p.properties.append(pos)
            messagebox.showinfo("Buy Property", f"{p.name} bought {PROPERTY_NAMES[pos]}!")
            # Draw a small rectangle to indicate ownership
            x1, y1, x2, y2 = self.space_coords[pos]
            self.canvas.create_rectangle(x1+5, y1+5, x1+20, y1+20, fill=p.color, tags="owner")
            self.update_info()
        else:
            messagebox.showinfo("Buy Property", "Not enough money!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MonopolyGUI(root, num_players=4)
    root.mainloop() 