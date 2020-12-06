
import csv

# Instatiate Scope Variables
rowValues = {}
headerValues = []

# Open and create CSV Dictionary
with open('example_skus.csv', newline='') as csvfile:
    skureader = csv.reader(csvfile, delimiter=',')
    for row in skureader:
        rowData = {
            'description': row[1],
            'sku': row[2]
        }
        rowValues[row[0]] = rowData

# Print Result Success
print(rowValues)