import pandas as pd

# Load the CSV data
data = pd.read_csv("data/03 cancer-death-rates-by-age.csv")

# Group data by entity and category, then calculate the sum of deaths
grouped_data = data.groupby(['Entity', 'Category']).sum().reset_index()

# Create separate dataframes for each category
categories = [
    'Deaths - Neoplasms - Sex: Both - Age: Under 5 (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 5-14 years (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 15-49 years (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 50-69 years (Rate)',
    'Deaths - Neoplasms - Sex: Both - Age: 70+ years (Rate)'
]

category_dataframes = {}

for category in categories:
    category_df = grouped_data[['Entity', category]]
    category_df.columns = ['Country', 'Death Rate']
    category_dataframes[category] = category_df

for category, category_df in category_dataframes.items():
    category_json = category_df.to_json(orient='records')
    
    # Save the JSON data to a file
    with open(f"{category}.json", "w") as json_file:
        json_file.write(category_json)
