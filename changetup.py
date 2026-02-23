originaltup=("Pizza","of",29)
index=int(input("Enter position of element in tuple you wnat to change: "))
index-=1
if originaltup[index] is int:
    change=int(input("Enter change: "))
else:
    change=input("Enter change: ")
templist=list(originaltup)
templist[index]=change
modifiedtup=tuple(templist)
print(modifiedtup)