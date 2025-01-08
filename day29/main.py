import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()    
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
img = tk.PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=1)

window.mainloop()