import math
try:
    x = 5
    assert x > 10
    a = 10
    a.append(5)
    data = input("Enter something: ")
    math.seterr(all='raise')
    y = math.sqrt(-1)
except AssertionError:
    print("AssertionError occurred")
except AttributeError:
    print("AttributeError occurred")
except EOFError:
    print("EOFError occurred")
except FloatingPointError:
    print("FloatingPointError occurred")
finally:
    print("Program finished")
