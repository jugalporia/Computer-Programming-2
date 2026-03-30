ventryd1={"Ramesh","Mukesh","Suresh"}
ventryd2={"Ramesh","Gukesh","Rajesh","Dexter"}
print("Visitors that visited both days:",ventryd1.intersection(ventryd2))
print("Visitors that visited only one day:",ventryd1.union(ventryd2)-ventryd1.intersection(ventryd2))
print("Unique visitors:",ventryd1.union(ventryd2))
