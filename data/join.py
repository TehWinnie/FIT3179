import pandas as pd

# Load your cancer death rates dataset into a DataFrame
df = pd.read_csv("average_death_rate_cancer_entity_grouped.csv")

# Load the latitude and longitude data from the second table into a DataFrame
location_df = pd.read_csv("countries.csv", usecols=["Country", "Latitude", "Longitude"])

# Merge the two DataFrames based on the "Entity" (or "Country") column
combined_df = df.merge(location_df, left_on="Entity", right_on="Country")

# Drop the duplicate "Country" column that comes from the merge
combined_df.drop(columns=["Country"], inplace=True)

# Save the combined DataFrame to a new CSV file if needed
combined_df.to_csv("final_cancer_location_data.csv", index=False)
