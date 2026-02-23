originaltup=("Pizza","of",29)
print(originaltup)
index=int(input("Enter position of element in tuple you wnat to delete: "))
index-=1
templist=list(originaltup)
templist.remove(templist[index])
modifiedtup=tuple(templist)
print(modifiedtup)