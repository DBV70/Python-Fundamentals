def calculate(operator, a: int, b: int):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b

input_operators = input()
first_num = int(input())
second_num = int(input())
result = calculate(input_operators, first_num, second_num)
print(int(result))
