import pandas as pd

df = pd.read_csv("data/formulation_data.csv")

print("\n--- firtst 5 rows ---")
print(df.head())

print("\n--- shape ---")
print(df.shape)

print("\n--- info ---")
df.info()

print("\n--- summary statistics ---")
print(df.describe())

print("\n--- missing values ---")
print(df.isna().sum())

