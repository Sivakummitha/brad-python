"""digits=[1,2,3]
for i in digits:
    for k in digits:
        for j in digits:
            print(i,j,k)"""
digits=[1,2,3]
for k in digits:
    for j in digits:
        for i in digits:
            if i!=k and k!=j and j!=i:
                print(i,j,k)
