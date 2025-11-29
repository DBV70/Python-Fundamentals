text = input()
final_string = ""
sub_string = ""
repetition = ""

for index in range(len(text)):
    if not text[index].isdigit():
        sub_string += text[index].upper()
    else:
        repetition += text[index]
        if index + 1 < len(text):
            if text[index + 1].isdigit():
                repetition += text[index + 1]
        final_string += sub_string * int(repetition)
        sub_string = ""
        repetition = ""

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)