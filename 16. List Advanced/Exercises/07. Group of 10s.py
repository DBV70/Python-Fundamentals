numbers = [int(number) for number in input().split(', ')]
group = 10

while len(numbers) > 0:
    current_group = list(filter(lambda number: number <= group, numbers))
    for number in current_group:
        numbers.remove(number)
    print(f"Group of {group}'s: {current_group}")
    group += 10
