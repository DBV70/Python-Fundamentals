number = int(input())

letters = [chr(ord('a') + i) for i in range(number)]

for first in letters:
    for second in letters:
        for third in letters:
            print(f"{first}{second}{third}")