import pandas as pd


#TODO 1. Create a dictionary in this format:
data = pd.read_csv("day30/nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato():
    user_input = list(input("Enter your Name: ").upper())
    phontic_words = [new_dict[letter] for letter in user_input]
    print(phontic_words)



onn = True
while onn:
    try:    
        nato()
        onn = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
