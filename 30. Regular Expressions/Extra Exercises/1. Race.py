import re

participants = input().split(', ')
ranklist = {}

while True:
    line = input()
    if line == "end of race":
        break

    name = ''.join(re. findall(r"[a-z]", line, re.IGNORECASE))
    if name not in participants:
        continue

    distance = sum(int(d) for d in re.findall(r"\d", line))
    if name not in ranklist:
        ranklist[name] = distance
    else:
        ranklist[name] += distance

sorted_ranklist = sorted(ranklist.items(), key=lambda x: (-x[1], x[0]))
ordinals = ['1st', '2nd', '3rd']
for i, (name, _) in enumerate(sorted_ranklist[:3]):
    print(f"{ordinals[i]} place: {name}")