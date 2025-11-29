words = input().split(" ")
dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for word, count in dictionary.items():
    if count % 2 != 0:
        print(word, end=" ")
