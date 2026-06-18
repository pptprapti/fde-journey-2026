employees = [
    "IT",
    "HR",
    "IT",
    "Finance",
    "IT",
    "HR"
]


def department_count(employees):
    department = {}

    for emp in employees:
        if emp in department:
            department[emp] += 1
        else:
            department[emp] = 1

    return department

departments_count = department_count(employees)

print(departments_count)
