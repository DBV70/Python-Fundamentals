def positive_numbers(some_numbers: list) -> str:
    return ", ".join([number for number in some_numbers if int(number) >= 0])

def negative_numbers(some_numbers: list) -> str:
    return ", ".join([number for number in some_numbers if int(number) < 0])

def even_numbers(some_numbers: list) -> str:
    return ", ".join([number for number in some_numbers if int(number) % 2 == 0])

def odd_numbers(some_numbers: list) -> str:
    return ", ".join([number for number in some_numbers if int(number) % 2 != 0])

numbers = input().split(', ')

print(f'Positive: {positive_numbers(numbers)}')
print(f'Negative: {negative_numbers(numbers)}')
print(f'Even: {even_numbers(numbers)}')
print(f'Odd: {odd_numbers(numbers)}')
