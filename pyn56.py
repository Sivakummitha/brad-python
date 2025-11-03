import csv
fields = ['Name', 'Email']
rows = [ ['Nikhil', 'nikhil.gfg@gmail.com'],
        ['Sanchit', 'siva.gfg@gmail.com'],
        ['Aditya', 'charan.gfg@gmail.com'],
        ['Sagar', 'sagar.gfg@gmail.com'],
        ['Prateek', 'prateek.gfg@gmail.com'],
        ['Sahil', 'sahil.gfg@gmail.com']]
filename = "email_records.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)