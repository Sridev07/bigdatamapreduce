#!/usr/bin/env python3
import sys
import csv

# Read input from standard input
reader = csv.reader(sys.stdin)
next(reader)  # Skip the header

# For each row, output the brand and the sales value
for row in reader:
    brand = row[2]  # Assuming brand is the third column
    sales = row[4]  # Assuming sales is the fifth column
    print(f"{brand}\t{sales}")
