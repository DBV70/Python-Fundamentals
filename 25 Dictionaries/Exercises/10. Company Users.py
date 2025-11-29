companies = {}

while True:
    command = input()
    if command == "End":
        break

    company, employee_id = command.split(" -> ")
    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
