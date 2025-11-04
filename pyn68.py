import json
import csv
data = [
    {"name": "Siva", "age": 22, "city": "Hyderabad"},
    {"name": "Charan", "age": 23, "city": "Chennai"}
]
f = open("data.json", "w")
json.dump(data, f)
f.close()
f = open("data.json", "r")
d = json.load(f)
f.close()
f = open("data.csv", "w", newline="")
w = csv.DictWriter(f, fieldnames=d[0].keys())
w.writeheader()
w.writerows(d)
f.close()
f = open("data.csv", "r")
r = csv.DictReader(f)
rows = list(r)
f.close()
f = open("new.json", "w")
json.dump(rows, f, indent=4)
f.close()
print("Done")

