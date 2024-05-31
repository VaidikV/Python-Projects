import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(key)
    # print(value)
    pass

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # print(index)
    # print(row)
    # Access row.student or row.score
    # print(row.student)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dataframe = pandas.DataFrame(nato_csv)

nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()

# user_nato_list = [code for item in user_input for (letter, code) in nato_dict.items() if item == letter]

# user_nato_list = [nato_dict[letter] for letter in user_input]
user_nato_list = [nato_dict[letter] if letter in nato_dict else letter for letter in user_input]
print(user_nato_list)
