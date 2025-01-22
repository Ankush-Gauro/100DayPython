import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_card = {}
words_to_learn = {}

try:
    data = pd.read_csv("day31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("day31/data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_front, image=card_front)
    flip_timer = window.after(3000, flip)

def flip():
    global current_card
    canvas.itemconfig(canvas_front, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    global current_card
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("day31/data/words_to_learn.csv", index=False)
    next_card()


flip_timer = window.after(3000, flip)
card_front = tk.PhotoImage(file="day31/images/card_front.png")
card_back = tk.PhotoImage(file="day31/images/card_back.png")
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_front  = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)


wrong = tk.PhotoImage(file="day31/images/wrong.png")
wrong_button = tk.Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right = tk.PhotoImage(file="day31/images/right.png")
right_button = tk.Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)



card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


next_card()


window.mainloop()