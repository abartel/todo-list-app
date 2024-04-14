import csv

with open("files/weather.csv") as file:
    data = list(csv.reader(file))

city = input("Enter a wrestler: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
