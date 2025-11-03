import copy
'''a=[1,2,3,[2,3]]
b=(copy.copy(a))
b[3][0]="sivacharan"
print("original",a)
print("shallowcopy",b)'''
a=[1,2,3,[2,3]]
b=copy.deepcopy(a)
b[1]="amma"
print("original",a)
print("deepcopy:",b)

