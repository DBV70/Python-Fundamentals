strings = input().split()
result = [text * len(text) for text in strings]

print(''.join(result))
