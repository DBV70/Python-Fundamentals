passwords = {}
submissions = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    passwords[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    submission, password, username, points = command.split("=>")
    points = int(points)
    if submission in passwords and password == passwords[submission]:
        if username not in submissions:
            submissions[username] = {}
        if submission not in submissions[username]:
            submissions[username][submission] = 0
        if points > submissions[username][submission]:
            submissions[username][submission] = points

best_candidate = ""
best_total = 0
for username, contests in submissions.items():
    total = sum(contests.values())
    if total > best_total:
        best_candidate = username
        best_total = total
print(f"Best candidate is {best_candidate} with total {best_total} points.")

print("Ranking:")
for username in sorted(submissions.keys()):
    print(f"{username}")
    for contest_name, pts in sorted(submissions[username].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest_name} -> {pts}")