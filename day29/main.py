import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for x in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for x in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for x in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    passkey = password_entry.get()
    email = email_username_entry.get()
    all_data = f"{web} | {email} | {passkey}\n"

    if len(web) == 0 or len(passkey) == 0:
        tk.messagebox.showinfo(title="Password Manager", message="Please don't leave any fields empty!")
        return

    is_okay = tk.messagebox.askokcancel(title = "Password Manager" , message =f"These are the details entered: \nEmail: {email}\nPassword: {passkey}\nIs it okay to save?")
    
    if is_okay:
        with open("day29/data.txt", "a") as file:
            file.write(all_data)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()    
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
img = tk.PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:", font=("Arial", 12))
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=54)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


email_username_label = tk.Label(text="Email/username:", font=("Arial", 12))
email_username_label.grid(column=0, row=2)

email_username_entry = tk.Entry(width=54)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "agauro@myseneca.ca")


password_label = tk.Label(text="Password:", font=("Arial", 12))
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", font=("Arial", 10), command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", font=("Arial", 10), width=40, command=save)

add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()