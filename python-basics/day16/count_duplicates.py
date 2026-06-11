word = input("Enter any word: ")
word = word.lower()
frequency = {}

for ch in word:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

dup_value_check = 1
dup_count = 0 

for ch in frequency:
    if frequency[ch] > dup_value_check:
         dup_count = dup_count + 1 



print(f"The characters which are dupliacte: {dup_count}")
