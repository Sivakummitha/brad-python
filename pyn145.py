from pathlib import Path
file = Path.home() / "Desktop" / "hello.txt"
file.write_text("Hello World")
print("File created at:", file)

