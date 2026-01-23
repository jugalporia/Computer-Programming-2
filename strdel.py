string1=input("Enter a string: ")
delstring=input("Enter part of string you want to delete from string: ")
if delstring in string1:
	print( string1.replace(delstring , "") )
else:
	print("The string part you want to delete doesn't exist inside entered string.")