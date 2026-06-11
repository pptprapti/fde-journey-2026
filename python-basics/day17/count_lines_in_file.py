file = open("day17\\sample.txt", "r")

count = 0

for line in file:
    count = count + 1

print(f"total no of lines are: {count}")

file.close()