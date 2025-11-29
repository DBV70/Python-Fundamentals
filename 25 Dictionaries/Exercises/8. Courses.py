courses = {}

while True:
    command = input()
    if command == "end":
        break

    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
