def perfect_number(number):
    aliquot_sum = 0
    for divisor in range(1, number - 1):
        if number % divisor == 0:
            aliquot_sum += divisor
    if aliquot_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

input_number = int(input())
print(perfect_number(input_number))