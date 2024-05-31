PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as general_letter:
    general_letter_contents = general_letter.read()
    for name in name_list:
        stripped_name = name.strip('\n')
        edited_letter = general_letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Invitation_for_{stripped_name}", mode="w") as final_letter:
            final_letter.write(edited_letter)
