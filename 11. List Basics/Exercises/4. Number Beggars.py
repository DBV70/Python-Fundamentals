numbers = input().split(', ')
beggars = int(input())
beggars_sum = []

for beggar in range(beggars):
    beggar_sum = 0
    for number in range(beggar, len(numbers), beggars):
        beggar_sum += int(numbers[number])
    beggars_sum.append(beggar_sum)

print(beggars_sum)