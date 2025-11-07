file = "example.txt"
word = "Python"
with open(file, 'r') as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))
    for i, line in enumerate(lines, start=1):
        if word in line:
            print(f"'{word}' found on line {i}")
