string=input("Enter a string: ")
v=0
c=0
for letters in string:
    if letters.lower() in "aeiou":
        v=v+1
    elif letters.lower() in "bcdfghjklmnpqrstvwxyz":
        c=c+1
print("Length of string:", len(string))
print("No. of vowels:", v, "\nNo. of consonants:", c)