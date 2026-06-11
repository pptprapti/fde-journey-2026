word = input("Enter any word: ")
word = word.lower()


no_of_occurence = {}
for ch in word:
    if ch in no_of_occurence:
        no_of_occurence[ch] = no_of_occurence[ch] + 1
    else:
        no_of_occurence[ch] = 1
     
most_char = ""
highest_count = 0 

for ch in no_of_occurence:
    if no_of_occurence[ch] > highest_count:
        highest_count = no_of_occurence[ch]
        most_char = ch 

print(f"Most frequent character is: {most_char}")
print(f"The number of occurence for {most_char} is: {highest_count}")