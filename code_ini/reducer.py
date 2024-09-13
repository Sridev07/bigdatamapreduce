#!/usr/bin/env python3
import sys

current_brand = None
lowest_sales = None
lowest_brand = None

# Read input from standard input
for line in sys.stdin:
    brand, sales = line.strip().split("\t")
    sales = int(sales)
    
    # Find the lowest sales for each brand
    if current_brand is None or sales < lowest_sales:
        current_brand = brand
        lowest_sales = sales
        lowest_brand = brand

# Output the brand with the lowest sales
if lowest_brand is not None:
    print(f"Lowest Sales: {lowest_sales} for brand {lowest_brand}")
