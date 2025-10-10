def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_division(a, b):
    return factorial(a) / factorial(b)

num1 = int(input())
num2 = int(input())
print(f"{factorial_division(num1, num2):.2f}")
