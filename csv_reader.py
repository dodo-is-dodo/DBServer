import csv

with open("data", "r") as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        print(row)
