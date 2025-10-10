people = list(map(int, input().split()))
k = int(input())
index = 0
killed_people = []

while people:
        index = (index + k - 1) % len(people)
        killed_people.append(people.pop(index))

print(f"[{','.join(map(str, killed_people))}]")