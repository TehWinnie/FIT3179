import pandas as pd

# Load your dataset into a DataFrame
df = pd.read_csv("06_number-of-people-with-cancer-by-age.csv")


# Group the data by the "Entity" column and sum the values for each age group
grouped = df.groupby("Entity")[["Prevalence - Neoplasms - Sex: Both - Age: 70+ years (Number)",
                                "Prevalence - Neoplasms - Sex: Both - Age: 50-69 years (Number)",
                                "Prevalence - Neoplasms - Sex: Both - Age: 15-49 years (Number)",
                                "Prevalence - Neoplasms - Sex: Both - Age: 5-14 years (Number)",
                                "Prevalence - Neoplasms - Sex: Both - Age: Under 5 (Number)"]].sum()

# Save the grouped data to a new CSV file
grouped.to_csv("total_death_cancer_entity_grouped.csv")
