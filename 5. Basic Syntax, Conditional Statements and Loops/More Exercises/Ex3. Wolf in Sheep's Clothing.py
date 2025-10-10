queue = input().split(", ")

wolf_index = queue.index("wolf")

if wolf_index == len(queue) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_number = len(queue) - wolf_index - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")