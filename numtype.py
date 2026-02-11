mynum=int(input("Enter a number: "))
print("The entered number is:\n")
flag=1

for i in range(2,mynum//2):
	if mynum%i==0:
		flag=0
		break

if flag==0:
    print("Not Prime.")
else:
    print("Prime.")

sum=0

for i in range(1,mynum):
	if mynum%i==0:
		sum+=i
if sum == mynum:
	print("Perfect number.")
else:
	print("Not Perfect number.")

armcount=len(str(mynum))
sum1=0
onum=mynum

for i in range(armcount):
    sum1 += pow(onum%10,armcount)
    onum=onum//10


if sum1==mynum:
	print("Armstrong.")
else:
	print("Not Armstrong.")


numstring=str(mynum)

if numstring[::-1]==numstring:
	print("Palindrome.")
else:
	print("Not Palindrome.")



