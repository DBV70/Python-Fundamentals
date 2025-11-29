students_dict = {}

while True:
    user_input = input()
    if user_input.islower():
        to_search = user_input.replace('_', ' ')
        break
    name, id, course = user_input.split(":")
    students_dict[id] = {'name': name, 'course': course}


for id, student in students_dict.items():
    if student['course'].lower() == to_search:
        print(f"{student['name']} - {id}")