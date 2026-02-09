stringlist=[]
print("Enter 5 strings:")
while len(stringlist)<5:
    mystring=input("Enter a string:")
    stringlist.append(mystring)

for i in range(len(stringlist)):
    stringlist[i]=stringlist[i].upper()
    
print(stringlist)