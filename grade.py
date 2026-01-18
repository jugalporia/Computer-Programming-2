print("Enter your marks to see grade:\n\n")
print("If absent for any subject enter \"-1\"")
s1=int(input("Enter marks of subject 1: "))
s2=int(input("Enter marks of subject 2: "))
s3=int(input("Enter marks of subject 3: "))
total=s1+s2+s3
avg=total/3
print("The total marks: ", total)
print("The average marks: ", avg)

if 0<s1<=39 or 0<s2<=39 or 0<s3<=39:
	print("You failed.")
elif s1==-1 or s2==-1 or s3==-1:
	print("Grade : N.A.")
elif 80<=avg<=100:
	print("Grade : O")
elif 70<=avg<=79:
	print("Grade : A+")
elif 60<=avg<=69:
	print("Grade : A")
elif 55<=avg<=59:
	print("Grade : B+")
elif 50<=avg<=54:
	print("Grade : B")
elif 45<=avg<=49:
	print("Grade : C")
elif 40<=avg<=44:
	print("Grade : P")
elif 0<=avg<=39:
	print("Grade : F")

