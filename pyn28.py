#write a program to Check if two strings are Rotationally Equivalent
def rotational_equivalent(string1,string2):
    if len(string1)!=len(string2):
        return False
    temparary=string1+string1
    if string2 in temparary:
        return True
    return False
rot_str=rotational_equivalent("banana","nabana")
print(rot_str)




    
