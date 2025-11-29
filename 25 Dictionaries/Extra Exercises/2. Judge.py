from itertools import count

contests = {}
total_scores = {}

while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}
    # participant in the contest
    if username not in contests[contest]:
        contests[contest][username] = points
        total_scores[username] = total_scores.get(username, 0) + points
    else:
        if points > contests[contest][username]:
            diff = points - contests[contest][username]
            contests[contest][username] = points
            total_scores[username] += diff

for each_contest in contests:
    print(f"{each_contest}: {len(contests[each_contest])} participants")
    i = 1
    for username, points in sorted(contests[each_contest].items(), key=lambda x: (-x[1], x[0])):
        print(f"{i}. {username} <::> {points}")
        i += 1
print("Individual standings:")
i = 1
for username, points in sorted(total_scores.items(), key=lambda x: (-x[1], x[0])):
    print(f"{i}. {username} -> {points}")
    i += 1
