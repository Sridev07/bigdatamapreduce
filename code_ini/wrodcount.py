import pandas as pd
from collections import defaultdict
file_path = r"C:\\Users\\Parth\\Downloads\\mobile_sales.csv"  # Use raw string or double backslashes
try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()
print("Column names in the dataset:", df.columns)
df.columns = df.columns.str.strip()
all_text = df.astype(str).apply(' '.join, axis=1).str.cat(sep=' ')
def map_function(text):
    words = text.split()  
    word_pairs = [(word.lower(), 1) for word in words]  
    return word_pairs
def reduce_function(mapped_data):
    word_count = defaultdict(int)  
    for word, count in mapped_data:
        word_count[word] += count  
    return word_count
def word_count(text):
    mapped_data = map_function(text)
    word_count_result = reduce_function(mapped_data)
    return word_count_result
word_count_result = word_count(all_text)
word_count_df = pd.DataFrame(word_count_result.items(), columns=['Word', 'Count'])
output_file_path = "C:\\Users\\Parth\\Desktop\\word_count_mobile_sales_output.csv"
word_count_df.to_csv(output_file_path, index=False)

print(f"Word count saved to '{output_file_path}'")
