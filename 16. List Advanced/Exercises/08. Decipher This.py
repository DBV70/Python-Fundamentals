message = input().split()
decoded_message = []

for each_word in message:
    coded_char = [int(x) for x in each_word if x.isdigit()]
    decoded_char = chr(int("".join(map(str, coded_char))))
    letters = [ch for ch in each_word if ch.isalpha()]
    letters[0], letters[-1] = letters[-1], letters[0]
    decoded_word = decoded_char + ''.join(letters)
    decoded_message.append(decoded_word)

print(' '.join(decoded_message))
