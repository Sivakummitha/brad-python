string=input("enter a string: ")
punctuations=",.&#$@%*^!?"
results=" "
for i in string:
    if i not in punctuations:
        results+=i
print(results)

        
