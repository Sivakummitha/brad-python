#"Write a program to print the following pattern using conditions

"""""A
B    C
D    E    F
G    H    I    J"""""
pattern= ord('A')
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if pattern <= ord('J'):
            print(chr(pattern), end=" ")
            pattern+= 1
        else:
            break  
    print() 

