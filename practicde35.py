a = [1, 2, 2, 3, 1, 4]
result = []
seen = set()

for x in a:
    if x not in seen:
        seen.add(x)
        result.append(x)

print(result)

    