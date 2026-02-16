lst=[
    (1,"Arti",19),
    (2,"Sam",19),
    (3,"Neha",20),
    (4,"Amit",20)
    ]
print("Original list: ", lst)
roll_lst=[]
name_lst=[]
age_lst=[]
for i in lst:
    roll_lst.append(i[0])
    name_lst.append(i[1])
    age_lst.append(i[2])
    
print("Roll number: ",roll_lst)
print("Name list: ",name_lst)
print("Age list: ",age_lst)