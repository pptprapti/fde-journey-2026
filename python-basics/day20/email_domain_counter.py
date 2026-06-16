emails = ["prapti@gmail.com",
    "rahul@yahoo.com",
    "anita@gmail.com",
    "aman@outlook.com",
    "riya@gmail.com"
]

domains = {}


for word in emails: 
    parts = word.split("@")
    domain = parts[1]
    if domain in domains:
        domains[domain] = domains[domain] + 1
    else:
        domains[domain] = 1

print(f"{domains}")