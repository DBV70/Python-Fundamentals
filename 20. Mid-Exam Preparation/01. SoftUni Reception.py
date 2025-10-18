from math import ceil

employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students_count = int(input())

students_per_hour = employee_1 + employee_2 + employee_3

if students_per_hour == 0:
    time = 0
else:
    working_hours = ceil(students_count / students_per_hour) if students_count > 0 else 0
    breaks = (working_hours - 1) // 3 if working_hours > 0 else 0
    time = working_hours + breaks

print(f"Time needed: {time}h.")