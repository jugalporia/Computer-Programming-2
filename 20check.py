mylist=[]
import random
while len(mylist)<20:
    mylist.append(random.randint(1,100))
    
print(mylist)
check=int(input("Enter a number: "))

print(mylist.count(check))