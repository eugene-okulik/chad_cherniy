import csv

with open('data.csv', newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)


for row in data:
    last_name, name, city = row
    print(f'Name: {name}, Last name: {last_name}, City: {city}')

with open('data.csv', newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        if row['last'] == 'Okulik':
            data.append(row)


for row in data:
    print(row)
