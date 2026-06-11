word = "banana"

frequency = {}

for ch in word:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

print(frequency)