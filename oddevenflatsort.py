oddlist=[]
evenlist=[]
import random
while len(oddlist)<5:
    myint=random.randint(1,100)
    if not myint%2==0:
        oddlist.append(myint)

while len(evenlist)<4:
    myint=random.randint(1,100)
    if myint%2==0:
        evenlist.append(myint)
        
print("odd list:",oddlist)
print("even list:",evenlist)

oddlist.remove(oddlist[2])
oddlist.insert(2,evenlist)

print("Even list inserted in odd list: ",oddlist)

oddlist.remove(oddlist[2])

for number in evenlist:
    oddlist.append(number)
    
oddlist.sort()

print("Sorted and flattened list:",oddlist)