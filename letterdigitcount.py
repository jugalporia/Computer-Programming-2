string=input("Enter a string:\n")
dcount=lcount=0
for letter in string:
	if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
		lcount+=1
	elif letter in "0123456789":
		dcount+=1
print("No. of letters:",lcount,"\nNo. of digits:", dcount)