import re

words_string = input()
pattern = r"([@#])([A-za-z]{3,})\1{2}([A-za-z]{3,})\1"
mirror_words = []
matches = re.findall(pattern, words_string)
for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
