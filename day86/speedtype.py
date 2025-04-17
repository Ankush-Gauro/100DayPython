import tkinter as tk

from tkinter import messagebox

import time

import random



# Sample texts to choose from randomly

sample_texts = [

    "The quick brown fox jumps over the lazy dog.",

    "Typing fast is a useful skill in the digital age.",

    "Practice makes perfect when learning how to type.",

    "Python is a fun and powerful programming language.",

    "Speed and accuracy are both important in typing."

]



root = tk.Tk()

root.title("Typing Speed Test")

root.geometry("700x450")



start_time = 0

current_text = ""



# Functions

def start_test():

    global start_time, current_text

    typing_area.delete("1.0", tk.END)

   

    # Pick random text

    current_text = random.choice(sample_texts)

    text_display.config(text=current_text)

   

    # Reset highlighting

    typing_area.tag_delete("correct")

    typing_area.tag_delete("incorrect")

   

    start_time = time.time()

    start_button.config(state="disabled")

    done_button.config(state="normal")



def end_test():

    global start_time, current_text

    end_time = time.time()

    typed_text = typing_area.get("1.0", tk.END).strip()

    total_time = end_time - start_time

   

    word_count = len(typed_text.split())

    wpm = round(word_count / (total_time / 60)) if total_time > 0 else 0



    # Highlight correct/incorrect words

    highlight_words(typed_text, current_text)



    messagebox.showinfo("Result", f"Your typing speed is {wpm} words per minute.")

    start_button.config(state="normal")

    done_button.config(state="disabled")



def highlight_words(typed, reference):

    typed_words = typed.split()

    reference_words = reference.split()



    typing_area.tag_config("correct", foreground="green")

    typing_area.tag_config("incorrect", foreground="red")



    index = "1.0"

    for i in range(len(typed_words)):

        word = typed_words[i]

        try:

            correct_word = reference_words[i]

        except IndexError:

            correct_word = ""



        # Find the start and end index of each word in the text widget

        word_start = typing_area.search(word, index, tk.END)

        if not word_start:

            continue

        word_end = f"{word_start}+{len(word)}c"

       

        if word == correct_word:

            typing_area.tag_add("correct", word_start, word_end)

        else:

            typing_area.tag_add("incorrect", word_start, word_end)

       

        index = word_end  # Move to next word



# GUI Layout

instruction_label = tk.Label(root, text="Type the following text as fast and accurately as you can:", font=("Arial", 14))

instruction_label.pack(pady=10)



text_display = tk.Label(root, text="", wraplength=600, font=("Arial", 12), justify="center")

text_display.pack(pady=10)



typing_area = tk.Text(root, height=8, width=80, font=("Arial", 12), wrap="word")

typing_area.pack(pady=10)



button_frame = tk.Frame(root)

button_frame.pack()



start_button = tk.Button(button_frame, text="Start", command=start_test, width=10)

start_button.grid(row=0, column=0, padx=20, pady=10)



done_button = tk.Button(button_frame, text="Done", command=end_test, state="disabled", width=10)

done_button.grid(row=0, column=1, padx=20, pady=10)



root.mainloop()