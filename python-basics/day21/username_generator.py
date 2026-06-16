employees = [
    "Prapti Sinha",
    "Rahul Sharma",
    "Anita Verma"
]
final_usernames =[]

for emp in employees:
    emp = emp.lower()
    parts = emp.split(" ")
    first_name = parts[0]
    last_name = parts[1]
    username = first_name[0] + last_name
    if username not in final_usernames:
       final_usernames.append(username)
print(final_usernames)

    



