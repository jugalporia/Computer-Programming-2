mylist=[]
import random
while len(mylist)<50:
    mylist.append(random.randint(1,30))
    
print("Generated list: ", mylist)

mylist=list(set(mylist))
mylist.sort()

print("Deleted duplicate list: ",mylist)