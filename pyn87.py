try:
    print("Before SystemExit")
    raise SystemExit("Exiting the program manually...")
except SystemExit as e:
    print("Caught SystemExit Exception:", e)
try:
    value = "10" + 5
except TypeError as e:
    print("Caught TypeError Exception:", e)
def demo_unboundlocal():
    try:
        x = 10
        def inner():
            print(x)
            x = x + 1
        inner()
    except UnboundLocalError as e:
        print("Caught UnboundLocalError Exception:", e)
demo_unboundlocal()
try:
    text = "Python ❤️"
    encoded = text.encode("ascii")
except UnicodeError as e:
    print("Caught UnicodeError Exception:", e)


