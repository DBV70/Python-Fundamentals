initial_list = input().split(', ')
num_list = list(map(int, initial_list))

for each in num_list:
    if each == 0:
        num_list.remove(each)
        num_list.append(0)

print(num_list)
