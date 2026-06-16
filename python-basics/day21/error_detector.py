logs = [
    "INFO",
    "INFO",
    "ERROR",
    "INFO"
]
has_error = False
for log in logs:
    log = log.lower()
    if log == "error":
        has_error = True
        break

if has_error == True:
    print("ERROR FOUND")