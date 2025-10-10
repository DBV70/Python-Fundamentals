cards = input().split()
shuffles = int(input())
left_split = []

for iteration in range(shuffles):
    left_split.clear()
    right_split = cards.copy()
    for i in range(len(cards) // 2):
        left_split.append(cards[i])
        right_split.remove(cards[i])

    cards.clear()
    for i in range(len(left_split)):
        cards.append(left_split[i])
        cards.append(right_split[i])

print(cards)