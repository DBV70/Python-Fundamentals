numbers = [int(num) for num in input().split()]
average = sum(numbers) / len(numbers)

filtered_numbers = list(filter(lambda x: x > average, numbers))
filtered_numbers.sort(reverse=True)
top_5 = filtered_numbers[:5]

if len(top_5) > 0:
    print(' '.join(map(str, top_5)))
else:
    print("No")