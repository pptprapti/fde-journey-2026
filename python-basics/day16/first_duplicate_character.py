word = input("Enter any word: ")
word = word.lower()

character = input("Enter the character to check its duplicacy: ")
character = character.lower()
frequency = {}

for ch in word:
    if ch in frequency:
        print(f" The first duplicate for the {character} has occured. ")
        break
    else:
        frequency[ch] = True

    