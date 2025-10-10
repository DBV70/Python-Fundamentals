nums = list(map(int, input().split()))

def exchange(nums, idx):
    if 0 <= idx < len(nums):
        return nums[idx+1:] + nums[:idx+1]
    else:
        print("Invalid index")
        return nums

def max_even_odd(nums, parity):
    filtered = [n for n in nums if n % 2 == (0 if parity == "even" else 1)]
    if not filtered:
        print("No matches")
        return
    max_val = max(filtered)
    # rightmost index
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == max_val and nums[i] % 2 == (0 if parity == "even" else 1):
            print(i)
            return

def min_even_odd(nums, parity):
    filtered = [n for n in nums if n % 2 == (0 if parity == "even" else 1)]
    if not filtered:
        print("No matches")
        return
    min_val = min(filtered)
    # rightmost index
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == min_val and nums[i] % 2 == (0 if parity == "even" else 1):
            print(i)
            return

def first_count(nums, count, parity):
    if count > len(nums):
        print("Invalid count")
        return
    result = [n for n in nums if n % 2 == (0 if parity == "even" else 1)]
    print(result[:count])

def last_count(nums, count, parity):
    if count > len(nums):
        print("Invalid count")
        return
    result = [n for n in nums if n % 2 == (0 if parity == "even" else 1)]
    print(result[-count:] if count != 0 else [])

while True:
    command = input()
    if command == "end":
        break
    parts = command.split()
    if parts[0] == "exchange":
        idx = int(parts[1])
        nums = exchange(nums, idx)
    elif parts[0] == "max":
        max_even_odd(nums, parts[1])
    elif parts[0] == "min":
        min_even_odd(nums, parts[1])
    elif parts[0] == "first":
        count = int(parts[1])
        first_count(nums, count, parts[2])
    elif parts[0] == "last":
        count = int(parts[1])
        last_count(nums, count, parts[2])

print(nums)