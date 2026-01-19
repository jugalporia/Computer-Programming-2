string=input("Enter a string: ")
v=0
for letters in string:
    if letters in 'aeiouAEIOU':
        v=v+1
print(v)
