listoftup=[("Burger", 29),(),("Ice cream", 10)]
newtuplist=[]
for tup in listoftup:
    if len(tup)==0:
        continue
    else:
        newtuplist.append(tup)
print(newtuplist)
    