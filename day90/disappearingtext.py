import tkinter as tk

DISAPPEAR_TIME = 5000  # 5 seconds in milliseconds

class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text App")

        self.text = tk.Text(root, height=10, width=40, font=("Arial", 14))
        self.text.pack(padx=20, pady=20)

        # Detect any key press in the text box
        self.text.bind("<Key>", self.reset_timer)

        self.timer = None

    def reset_timer(self, event=None):
        # Cancel existing timer if it's running
        if self.timer is not None:
            self.root.after_cancel(self.timer)
        # Start a new timer
        self.timer = self.root.after(DISAPPEAR_TIME, self.clear_text)

    def clear_text(self):
        self.text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()
