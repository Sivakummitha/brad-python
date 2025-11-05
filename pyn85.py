try:
    import math
    x = math.exp(1000)
except OverflowError:
    print("OverflowError occurred")
try:
    raise RuntimeError("Something went wrong")
except RuntimeError:
    print("RuntimeError occurred")
