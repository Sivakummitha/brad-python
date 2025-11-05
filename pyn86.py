#I referred this program from chatgpt i understood the logic then i proceeded
try:
    code = "x === 5"
    exec(code)
except SyntaxError:
    print("SyntaxError occurred")
try:
    exec("if True:\nprint('Hello')")
except IndentationError:
    print("IndentationError occurred")
try:
    exec("def test():\n\t    print('Hi')")
except TabError:
    print("TabError occurred")
try:
    raise SystemError("Internal system problem")
except SystemError:
    print("SystemError occurred")
print("Program finished")
