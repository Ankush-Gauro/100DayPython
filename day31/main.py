import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = tk.PhotoImage(file="day31/images/card_front.png")
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)


wrong = tk.PhotoImage(file="day31/images/wrong.png")
wrong_button = tk.Button(image=wrong, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right = tk.PhotoImage(file="day31/images/right.png")
right_button = tk.Button(image=right, highlightthickness=0)
right_button.grid(column=1, row=1)


data = pd.read_csv("day31/data/french_words.csv")
words = data.to_dict(orient="records")
current_word = random.choice(words)

canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text=current_word["French"], font=("Ariel", 60, "bold"))



window.mainloop()