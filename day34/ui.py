import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title = 'Quiz App'
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tk.Label(text = 'Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300,height=250, bg='white')
        self.question_text = self.canvas.create_text(150,125,text = "Question Text", fill=THEME_COLOR, font=("Arial", 20,'italic'), width=280)
        self.canvas.grid(row=1, column=0,columnspan=2, pady=30)
        true_image = tk.PhotoImage(file='day34/images/true.png')
        false_image = tk.PhotoImage(file='day34/images/false.png')
        self.true_button = tk.Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=1)
        self.false_button = tk.Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text= q_text)


