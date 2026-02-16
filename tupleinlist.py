lst=["Neha","Daya",("Vraj","Deven"),"Aarju",("Ramesh","Raju","Chaman")]
print("Original list: ",lst)
c1=0
c2=0
for i in lst:
    if isinstance(i, tuple):
        for j in i:
            c1+=1
    else:
        c2+=1
print("Number of boys: ",c1)
print("Number of girls: ",c2)