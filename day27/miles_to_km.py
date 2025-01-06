import tkinter as tk

window = tk.Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def calculate():
    miles = float(inp.get())
    km = round(miles * 1.6,2)
    output_label.config(text=f"{km}")

miles_label = tk.Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

inp = tk.Entry(width=10)
inp.grid(column=1, row=0)

is_equal_label = tk.Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)

output_label = tk.Label(text="0", font=("Arial", 12))
output_label.grid(column=1, row=1)

km_label = tk.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

calc = tk.Button(text="Calculate", command=calculate)
calc.grid(column=1, row=2)



window.mainloop()

