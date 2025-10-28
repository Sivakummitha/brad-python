#write a Python program to count the occurrence of each character in a word.
string=input("enter a word: ")
count={}
for i in string:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i,count in count.items():
    print(f"{i}:{count}")