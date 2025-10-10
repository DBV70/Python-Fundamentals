def rounding(numbers):
    rounded_numbers = []
    for number in numbers:
        rounded_numbers.append(round(number))
    return rounded_numbers

input_numbers = list(map(float, input().split()))
output_numbers = rounding(input_numbers)
print(output_numbers)
