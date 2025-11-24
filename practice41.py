def flatten(lst):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.extend(flatten(elem))   
        else:
            result.append(elem)
    return result
nested = [1, [2, 3], [4, [5, 6]]]
print(flatten(nested))
