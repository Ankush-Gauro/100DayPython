import tkinter

window = tkinter.Tk() # Create a window
window.title("GUI") # Set the title of the window
window.minsize(400,300)

my_label = tkinter.Label(text="Hello world", font=("Arial", 24, "bold"))
my_label.pack()
my_label['text'] = "New text"


def button_clicked():
    print("I got clicked")
    my_label.config(text=inp.get())

but = tkinter.Button(text="Click me", command=button_clicked)
but.pack()

inp = tkinter.Entry(width=10)
inp.pack()

window.mainloop()