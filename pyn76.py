#I referred this program from chatgpt i understood the logic then i proceeded
import re, os, sys
fname = "working.txt"
if not os.path.exists(fname):
    sample = """<html>
<a href="https://example.com">Example</a>
<a href='page.html'>Local page</a>
<a href="mailto:info@example.com">Mail</a>
</html>"""
    with open(fname, "w", encoding="utf-8") as f:
        f.write(sample)
    print(f"'{fname}' not found. Created sample '{fname}' (edit it if you want).")
try:
    with open(fname, "r", encoding="utf-8") as f:
        data = f.read()
except Exception as e:
    print("Cannot open file:", e)
    sys.exit(1)
links = re.findall(r'href=["\'](.*?)["\']', data, re.IGNORECASE)
out = "href_links.txt"
with open(out, "w", encoding="utf-8") as f:
    for link in links:
        f.write(link + "\n")

print(f"{len(links)} links extracted and saved to '{out}'")
