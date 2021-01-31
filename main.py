with open("./input/letters/starting_letter.txt") as file:
    letter_start = file.readlines()


with open("./input/names/invited_names.txt") as file:
    names = file.readlines()
previous_name = "[name]"
for name in names:

    name = name.strip('\n')
    appended_data = letter_start[0].replace(previous_name, name)
    letter_start[0] = appended_data
    previous_name = name
    with open(f"./output/readytosend/letter_to_{name}.txt", mode="w") as file:
        file.writelines(letter_start)

# TODO 1: Build out functionality to append the name to the letter and write the letter to a file
