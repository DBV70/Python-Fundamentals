string = input()

words = ['sand', 'water', 'fish', 'sun']
count = 0

lower_text = string.lower()
for word in words:
    count += lower_text.count(word)

print(count)
