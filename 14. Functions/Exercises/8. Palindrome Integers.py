def is_palindrome(number):
    return str(number) == str(number)[::-1]

numbers = list(map(int, input().split(", ")))
for number in numbers:
    print(is_palindrome(number))
