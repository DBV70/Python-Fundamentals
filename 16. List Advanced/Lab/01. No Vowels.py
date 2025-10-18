text = input()

new_list = [ch for ch in text if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(new_list))
