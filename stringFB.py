string=input("Enter a string: ")
i=0
print("Forward:")
while i<len(string):
	print(string[i])
	i+=1
print("Reverse:")
i=0
while i<len(string):
    print(string[len(string)-i-1])
    i+=1