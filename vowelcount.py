string1 = input("Enter a string to count its vowels: ")
v = 0

for letter in string1:
    if letter.lower() in "aeiou":
        v += 1

print("Number of vowels in the entered string are:", v)
