employees = {
    "Prapti": 92,
    "Rahul": 65,
    "Anita": 88,
    "Aman": 74
}

def performance_score(employees):
    new_emps = []
    for emp in employees:
        if employees[emp] > 80:
            emp1 = emp
            new_emps.append(emp1)

    return new_emps

result = performance_score(employees)

print(result)
