import re
text = """apple
banana
apple
mango
banana
orange
apple"""
unique_text = re.sub(r'(?m)^(.*)(\n\1)+$', r'\1', text)
print("Original Text:\n", text)
print("\nAfter Removing Duplicates:\n", unique_text)
