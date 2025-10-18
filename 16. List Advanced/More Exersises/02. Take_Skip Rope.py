string = input()

digits = [int(dig) for dig in string if dig.isdigit()]
letters =[ch for ch in string if not ch.isdigit()]

take_list = digits[::2]
skip_list = digits[1::2]

take_string = []
skip_string = []

index = 0
while index < len(take_list):
    for i in range(take_list[index]):
        if len(letters) == 0:
            break
        take_string.append(letters.pop(0))
    for j in range(skip_list[index]):
        if len(letters) == 0:
            break
        skip_string.append(letters.pop(0))
    index += 1

print(''.join(take_string))
