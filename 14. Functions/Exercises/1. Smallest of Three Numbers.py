def smallest(num1, num2, num3) -> int:
    numbers = [num1, num2, num3]
    smallest_number = min(numbers)
    return smallest_number

a = int(input())
b = int(input())
c = int(input())
result = smallest(a, b, c)
print(result)
