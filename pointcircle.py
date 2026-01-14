import math
r=int(input("Enter radius of circle: "))
x=int(input("Enter x coordinate of center of circle: "))
y=int(input("Enter y coordinate of center of circle: "))
print("Now enter the point you want to check for:\n")
x1=int(input("Enter x1 coordinate: "))
y1=int(input("Enter y1 coordinate: "))
d=math.sqrt(pow((x1-x),2)+pow((y1-y),2))

if d==r:
	print("The point is on the circle.")
elif d>r:
	print("The point is outside the circle.")
else:
	print("The point is inside the circle.")