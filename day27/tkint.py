import tkinter

window = tkinter.Tk() # Create a window
window.title("GUI") # Set the title of the window
window.minsize(400,300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="Hello world", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
my_label['text'] = "New text"


def button_clicked():
    print("I got clicked")
    my_label.config(text=inp.get())

but = tkinter.Button(text="Click me", command=button_clicked)
but.grid(column=1, row=1)


but2 = tkinter.Button(text="Click me again")
but2.grid(column=3, row=0)


inp = tkinter.Entry(width=10)
inp.grid(column=4, row=3)

window.mainloop()