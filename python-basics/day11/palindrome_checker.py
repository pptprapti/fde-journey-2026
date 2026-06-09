word = input ("Enter any word: ")

reverse = ""

for ch in word: 
    reverse = ch + reverse
    

if word == reverse:
    print(f" The word {word} is a Palindrome")
else:
    print(f"The word {word} is not a Palindrome") 