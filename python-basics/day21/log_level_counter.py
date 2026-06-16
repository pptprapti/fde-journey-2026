logs = [
    "INFO",
    "ERROR",
    "INFO",
    "WARNING",
    "ERROR",
    "ERROR"
]

frequency_logs = {}

for log in logs:
    if log in frequency_logs:
        frequency_logs[log] = frequency_logs[log] + 1
    else: 
        frequency_logs[log] = 1

print(f"Log frequency summary:: {frequency_logs}")