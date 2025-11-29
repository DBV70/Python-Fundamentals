results = {}
submissions = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    if "banned" in command:
        name = command.split("-")[0]
        del results[name]
        continue
    else:
        name, language, points = command.split("-")
        points = int(points)
        if name not in results:
            results[name] = {}
        if language not in results[name]:
            results[name][language] = points
        else:
            if points > results[name][language]:
                results[name][language] = points

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for name, languages in results.items():
    for language, points in languages.items():
        print(f"{name} | {points}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")