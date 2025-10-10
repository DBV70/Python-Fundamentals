number_of_characters = int(input())
char_sum = 0

for i in range(number_of_characters):
    letter = input()
    char_sum += ord(letter)

print(f'The sum equals: {char_sum}')
