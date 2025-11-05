#I referred this program from chatgpt i understood the logic then i proceeded
try:
    a = [1] * (10**10)
except MemoryError:
    print("MemoryError occurred")
try:
    print(x)
except NameError:
    print("NameError occurred")
try:
    raise NotImplementedError
except NotImplementedError:
    print("NotImplementedError occurred")
try:
    f = open("C:/no_such_folder/file.txt", "r")
except OSError:
    print("OSError occurred")

print("Program finished")
