word = input("Enter a word: ")
word = word.lower()

character = input("Enter a character: ")
character= character.lower()

found = False

for ch in word:
    if ch == character:
        found = True

if found:
    print("Character Found ")
else:
    print("Character not found")
