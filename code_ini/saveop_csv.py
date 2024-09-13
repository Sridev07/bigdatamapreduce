import pandas as pd

# Load the dataset
file_path = "C:\\Users\\Parth\\Downloads\\mobile_sales.csv"  # Update this with the correct path to your file
df = pd.read_csv(file_path)

# Convert the sales column to numeric (if necessary)
df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

# Remove rows with missing or invalid sales data
df = df.dropna(subset=['sales'])

# Find the row with the lowest sales
lowest_sales_row = df.loc[df['sales'].idxmin()]

# Extract the brand and sales value
lowest_sales_brand = lowest_sales_row['brand']
lowest_sales_value = lowest_sales_row['sales']

# Create a DataFrame with the results
result_df = pd.DataFrame({
    'Brand': [lowest_sales_brand],
    'Sales': [lowest_sales_value]
})

# Save the results to a CSV file
output_file_path ="C:\\Users\\Parth\\Downloads\\outputlowest.csv"  # Specify the desired output file path
result_df.to_csv(output_file_path, index=False)

print(f"Results have been saved to {output_file_path}.")
