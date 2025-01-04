import pandas as pd


#TODO 1. Create a dictionary in this format:
data = pd.read_csv("day26/nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter your Name: ").upper()
name_list = list(user_input)

phontic_words = [new_dict[letter] for letter in name_list]
print(phontic_words)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.