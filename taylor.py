radian=float(input("Enter a radian value:"))
import math
z=1
sum=0.0
for i in range(1,4):
	sum += pow(-1,i+1)*pow(radian,z)/math.factorial(z)
	z+=2

print(sum)