print("This program reports whether the area is greater than the perimeter of a rectangle with given parameters:\n\n")
l=int(input("Enter length of the rectangle: "))
b=int(input("Enter breadth of the rectangle: "))
A=l*b
P=2*(l+b)
if A>P:
	print("Area is greater than perimeter for given rectangle")
else:
	print("Area is less than perimeter for given rectangle")