import csv       
data = [['SN', 'Movie', 'director'],
        [1, 'baahubali-1', 'rajamouli'],
        [2, 'baahubali-2', 'rajamouli']]
with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
with open('zomato.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)  
    data_list = []  
    for row in csv_reader:
        data_list.append(row)
for data in data_list:
    print(data)