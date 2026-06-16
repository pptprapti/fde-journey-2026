user_logins = {
    "Prapti": 15,
    "Rahul": 0,
    "Anita": 7,
    "Aman": 0
}
inactive_users = []
for user in user_logins:
    login_count = user_logins[user]
    if login_count == 0:
        inactive_users.append(user)
    
print(f"Inactive Users are: {inactive_users}")
