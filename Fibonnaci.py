n=int(input("Enter a number"))
mylist=[0,1,1]
for i in range(n):
    print(mylist[i])
    if i>=2:
        mylist.append(mylist[i]+mylist[i-1])