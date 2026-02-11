numlist=[]
for i in range(1,31):
    numlist.append(i)
c=0
for k in range(len(numlist)):
    c=numlist[k]
    for i in range(len(numlist)):
        a=numlist[i]
        for j in range(i+1,len(numlist)-1):
            b=numlist[j]
            if pow(c,2) == pow(a,2) + pow(b,2):
                print("(", a, ",", b, ",", c, ")")