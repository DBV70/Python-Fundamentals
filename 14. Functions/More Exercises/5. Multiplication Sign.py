def multiplication_sign(a, b, c):
    nums = [a, b, c]
    if 0 in nums:
        print("zero")
        return
    negative_count = sum(1 for num in nums if num < 0)
    if negative_count % 2 == 0:
        print("positive")
    else:
        print("negative")

a = int(input())
b = int(input())
c = int(input())

multiplication_sign(a, b, c)