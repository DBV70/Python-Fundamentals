n = int(input())

for _ in range(n):
    line = input()
    name = ""
    age = ""

    at_index = line.index('@')
    pipe_index = line.index('|', at_index + 1) if at_index != -1 else -1
    if at_index != -1 and pipe_index != -1:
        name = line[at_index + 1:pipe_index]

    hash_position = line.index('#')
    star_index = line.index('*', hash_position + 1) if hash_position != -1 else -1
    if hash_position != -1 and star_index != -1:
        age = line[hash_position + 1:star_index]

    if name and age:
        print(f"{name} is {int(age)} years old.")
