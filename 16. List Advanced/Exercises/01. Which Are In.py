string_one = input().split(', ')
string_two = input().split(', ')

'Comprehension solution'
substring = [x for x in string_one if any(x in y for y in string_two)]
print(substring)

'Basic solution'
substring_b = []
for x in string_one:
    for y in string_two:
        if x in y:
            substring_b.append(x)
            break
print(substring_b)