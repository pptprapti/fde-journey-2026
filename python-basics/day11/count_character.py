word = input("Enter a word: ")

char = input("Enter a character to count: ")

count = 0 
word = word.lower()
char = char.lower()
for ch in word:
    if ch == char:
        count = count + 1
        
print(f" The total number of '{char}' characters present in the word {word} is: {count}")
