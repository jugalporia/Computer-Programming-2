import random
mylist=[]
plist=[]
nlist=[]
while len(mylist)<30:
    mylist.append(random.randint(-100,100))
    
for number in mylist:
    if number<0:
        nlist.append(number)
    else:
        plist.append(number)
        
print(mylist)
print("positive list: ",plist)
print("negative list: ",nlist)