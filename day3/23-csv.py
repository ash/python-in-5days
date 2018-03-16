# How you read from a CSV file

import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    # Just loop over the reader to get lines. Each line is a list containing the elements from a row.
    for row in reader:    
        print(row)
