text = input("Enter a string: ")
text = text.lower()
text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')

words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word frequency:", freq)

most_frequent = max(freq, key=freq.get)
print("Most frequent word:", most_frequent)