Price = {"apple": 29, "chocy milk": 37, "cheese": 150}
Quantity = {"apple": 0, "chocy milk": 2, "cheese": 1}

totalbill = 0

for item in Price:
    totalbill += Price[item] * Quantity[item]

print(totalbill)
