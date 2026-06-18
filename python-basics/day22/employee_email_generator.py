employees = [
    "Prapti Sinha",
    "Rahul Sharma",
    "Anita Verma",
    "Aman Gupta"
]

def employee_email_generator(employees):
    emp_emails = []
    for emp in employees:
        parts = emp.split(" ")
        first_name = parts[0].lower()
        last_name = parts[1].lower()
        email = first_name + "." + last_name + "@company.com"
        emp_emails.append(email)

    return emp_emails

result = employee_email_generator(employees)

print(result)