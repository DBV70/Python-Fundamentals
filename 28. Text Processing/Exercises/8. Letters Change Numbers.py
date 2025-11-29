all_strings = input().split()
total_sum = 0

for string in all_strings:
    front_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:len(string) - 1])
    if front_letter.isupper():
        front_letter_position = ord(front_letter) - 64
        total_sum += number / front_letter_position
    elif front_letter.islower():
        front_letter_position = ord(front_letter) - 96
        total_sum += number * front_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position

print(f"{total_sum:.2f}")
