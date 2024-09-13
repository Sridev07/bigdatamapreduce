import pandas as pd

# Load the provided dataset
file_path = "C:\\Users\\Parth\\Downloads\\mobile_sales.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()
