text = input()

indices = [i for i, char in enumerate(text) if char.isupper()]

print(indices)
