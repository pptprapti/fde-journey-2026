salaries = [45000, 52000, 61000, 48000]

high_sal_found = False

for sal in salaries:
    if sal > 60000:
        high_sal_found = True
        break

if high_sal_found == True:
    print("HIGH SALARY FOUND")
else:
    print("NO HIGH SALARY FOUND")
