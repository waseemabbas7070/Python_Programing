import csv
with open('weatherAUS.csv', mode ='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)