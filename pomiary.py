import csv

with open("Raw Data.csv") as data:
    data = csv.reader(data)
    for row in data:
        print(row)
