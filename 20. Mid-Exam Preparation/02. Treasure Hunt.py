def loot(current_chest:list, current_items:list) -> list:
    for i in range(1, len(current_items)):
        if current_items[i] not in current_chest:
            current_chest.insert(0,current_items[i])
    return current_chest

def drop(current_chest:list, current_index:int) -> list:
    if current_index in range(len(current_chest)):
        current_chest.append(current_chest.pop(current_index))
    return current_chest

def steal(current_chest:list, current_count:int) -> list:
    if current_count >= len(current_chest):
        print(', '.join(current_chest))
        current_chest = []
    else:
        stealing_index = len(current_chest) - current_count
        print(', '.join(current_chest[stealing_index:]))
        current_chest = current_chest[:stealing_index]
    return current_chest

treasure_chest = input().split("|")
items = input().split()
while not items[0] == "Yohoho!":
    if items[0] == "Loot":
        treasure_chest = loot(treasure_chest, items)
    elif items[0] == "Drop":
        index = int(items[1])
        treasure_chest = drop(treasure_chest, index)
    elif items[0] == "Steal":
        count = int(items[1])
        treasure_chest = steal(treasure_chest, count)
    items = input().split()

if not treasure_chest:
    print("Failed treasure hunt.")
else:
    average_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
