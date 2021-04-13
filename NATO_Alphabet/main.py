import pandas as pd

student_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a data frame
nato_alphabet = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}


word = input("Enter the word").upper()

new_list = []
for letter1 in word:
    result = [value for (key, value) in nato_alphabet.items() if key == letter1]
    new_list.extend(result)
print(new_list)

