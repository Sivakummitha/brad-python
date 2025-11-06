#I referred this program from chatgpt i understood the logic then i proceeded
try:
    text = "Python ❤️"
    encoded = text.encode("ascii")
except UnicodeEncodeError as e:
    print("Caught UnicodeEncodeError Exception:", e)
try:
    byte_data = b'\xff'
    decoded = byte_data.decode("utf-8")
except UnicodeDecodeError as e:
    print("Caught UnicodeDecodeError Exception:", e)
try:
    text = "Python ❤️"
    result = text.encode("utf-8").decode("ascii")
except UnicodeTranslateError as e:
    print("Caught UnicodeTranslateError Exception:", e)
