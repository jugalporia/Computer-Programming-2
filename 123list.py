firstlist=[1,2,3,9,10,11]
secondlist=[2,9,10,12,13]
thirdlist=[i for i in firstlist if i not in secondlist]
print(thirdlist)