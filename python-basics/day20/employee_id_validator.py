employee_ids = ["EMP101","EMP102","EMP101","EMP103","EMP102"]

frequency = {}

for ch in employee_ids:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for ch in frequency:
    if frequency[ch] > 1:
        print(f"Duplicate Employee IDs {ch}")