string1=input("Enter first string: ")
string2=input("Enter second string:")
if string1 in string2:
	print("First string exists inside second string.")
elif string2 in string1:
	print("Second string exists inside first string.")