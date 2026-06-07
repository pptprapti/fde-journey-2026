numbers = [10,20,30,40]
target = 30 
flag = False
for num in numbers:
    if num == target:
        flag = True
        print("Found")
if flag == False:
    print("Not FOund")

