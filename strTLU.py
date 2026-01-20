string=input("Enter a string: ")
stringl=""
stringu=""
stringt=""

#Lower case string
for letter in string:
	if 65<=ord(letter)<=90:
		stringl = stringl + chr(ord(letter)+32)
	else:
	    stringl = stringl + letter
	    
#Upper case string
for letter in string:
	if 97<=ord(letter)<=122:
		stringu = stringu + chr(ord(letter)-32)
	else:
	    stringu = stringu + letter
	    
#toggle case string
for letter in string:
	if 65<=ord(letter)<=90:
		stringt = stringt + chr(ord(letter)+32)
	elif 97<=ord(letter)<=122:
		stringt = stringt + chr(ord(letter)-32)
	else:
	    stringt = stringt + letter

print("lower case:",stringl)
print("upper case:",stringu)
print("toggle case:",stringt)