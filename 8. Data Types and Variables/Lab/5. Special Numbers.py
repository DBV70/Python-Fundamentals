n = int(input())
special_numbers = [5, 7, 11]

for number in range(1, n + 1):
    digit_sum = sum(int(digit) for digit in str(number))
    print(f'{number} -> {digit_sum in special_numbers}')
