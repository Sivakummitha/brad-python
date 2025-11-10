with open("pyn103.py","r")as f1:
    data1=f1.read()
with open("pyn104.py","r")as f2:
    data2=f2.read()
with open("mergedfile.py","w")as f3:
    f3.write(data1+data2)
print("merged data created successfully")
