def unique_union(list1, list2):
    result = []
    for x in list1:
        if x not in result:
            result.append(x)
    for x in list2:
        if x not in result:
            result.append(x)
    return result
print(unique_union([1,2,3,4], [3,4,5,6]))
