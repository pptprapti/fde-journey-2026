word = input("Enter a word: ")

reverse = ""

for ch in word:
    reverse =  ch + reverse
print(reverse)