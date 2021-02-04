PLACEHOLDER = "[name]"

with open("names.txt") as names:
    names = names.readlines()
print(names)

with open("message.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, name)
        with open(f"letter for {stripped_name}", mode="w") as f:
            f.write(new_letter)

