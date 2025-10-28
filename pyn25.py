#write a program to Extract Indices of substring matches
string=input("enter a string : ")
sub_string=input("enter a substring: ")
indices=[]
for i in range(len(string)-len(sub_string)+1):
    if string[i:i+len(sub_string)]==sub_string:
        indices.append(i)
print(indices)