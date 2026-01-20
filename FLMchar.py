string=input("Enter a string: ")
print("First character: ", string[0])
print("Last character: ", string[-1])
if len(string)%2!=0:
    print("Middle character: ", string[len(string)//2])