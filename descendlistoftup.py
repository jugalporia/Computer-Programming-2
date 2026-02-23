listoftup=[("Burger", 29),("Pizza", 30),("Ice cream", 10)]
swap= None
z=len(listoftup)-2
while z>0:
    for i in range(len(listoftup)-1):
        if listoftup[i][1]<listoftup[i+1][1]:
            swap=listoftup[i]
            listoftup[i]=listoftup[i+1]
            listoftup[i+1]=swap
    z-=1
print(listoftup)