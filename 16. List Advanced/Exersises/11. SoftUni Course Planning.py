schedule = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')
    if "Add" in command:
        lesson_title = command[1]
        if not lesson_title in schedule:
            schedule.append(lesson_title)
    elif "Insert" in command:
        lesson_title = command[1]
        index = int(command[2])
        if not lesson_title in schedule and 0 <= index <= len(schedule):
            schedule.insert(index, lesson_title)
    elif "Remove" in command:
        lesson_title = command[1]
        if lesson_title in schedule:
            schedule.remove(lesson_title)
    elif "Swap" in command:
        lesson_title_1 = command[1]
        lesson_title_2 = command[2]
        if lesson_title_1 in schedule and lesson_title_2 in schedule:
            idx1 = schedule.index(lesson_title_1)
            idx2 = schedule.index(lesson_title_2)
            schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]
            exercise1 = f"{lesson_title_1}-Exercise"
            exercise2 = f"{lesson_title_2}-Exercise"
            if idx1 + 1 < len(schedule) and schedule[idx1 + 1] == exercise1:
                schedule.remove(exercise1)
                schedule.insert(idx2 + 1, exercise1)
            if idx2 + 1 < len(schedule) and schedule[idx2 + 1] == exercise2:
                schedule.remove(exercise2)
                schedule.insert(idx1 + 1, exercise2)
    elif "Exercise" in command:
        lesson_title = command[1]
        if lesson_title in schedule:
            a = schedule.index(lesson_title)
            schedule.insert(a + 1, lesson_title + '-Exercise')
        else:
            schedule.append(lesson_title)
            schedule.append(lesson_title + '-Exercise')

    command = input()

for each in schedule:
    print(f'{schedule.index(each) + 1}.{each}')
