def count_lower_upper(string):
    upcount=0
    lcount=0
    for letter in string:
        if letter.isupper():
            upcount+=1
        else:
            lcount+=1
    mydict={"upper count": upcount, "lower count": lcount}
    return mydict
mystring=input("Enter a string:")
print(count_lower_upper(mystring))

    
