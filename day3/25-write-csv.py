# A tool to convert a JSON file to a CSV file.
# The input file keeps the data in the following format:
# [{"date":"2014-07-31","price":1000},{"date":"2014-08-01","price":1018.2027},{"date":"2014-08-02","price":1008.7724},...

import csv
import json
import sys

# We take the filenames from the command line.
# Notice that if you run it as:
# python3 25-write-csv.py a.json b.csv
# then the first filename will be in the element 1.
in_file = sys.argv[1]
out_file = sys.argv[2]

# Load and parse JSON:
data = []
with open(in_file) as f:
    data = json.load(f)

# Iterate over it to print it line by line.
with open(out_file, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=':')
    # For the header, just take the first element from data
    writer.writerow(data[0].keys())
    for row in data:
        writer.writerow(row.values())
