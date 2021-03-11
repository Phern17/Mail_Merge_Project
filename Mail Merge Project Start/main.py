PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_in:
    guest_list = name_in.readlines()

with open("./Input/Letters/starting_letter.txt") as fin:
    data = fin.read()
    for name in guest_list:
        new_name = name.strip()
        output = data.replace(PLACEHOLDER, new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as f_out:
            f_out.writelines(output)






