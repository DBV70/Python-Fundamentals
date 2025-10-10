def odd_even_sum(numbers: str) -> str:
    odd_sum = 0
    even_sum = 0
    for number in numbers:
            odd_sum += int(number) if int(number) % 2 != 0 else 0
            even_sum += int(number) if int(number) % 2 == 0 else 0

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()
print(odd_even_sum(number))
