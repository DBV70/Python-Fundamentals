def sum_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b

def add_and_subtract(a, b, c):
    result = subtract(sum_numbers(a, b), c)
    return result

a = int(input())
b = int(input())
c = int(input())
output = add_and_subtract(a, b, c)
print(output)
