# task1_data_cleaning.py

import pandas as pd

# 1. Load dataset
df = pd.read_csv(r"C:\Users\hsush\OneDrive\Documents\Desktop\marketing_campaign.csv")

print("Initial Shape:", df.shape)

# 2. Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Handle missing values: fill numeric with mean, text with mode
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

# 3. Remove duplicates
df.drop_duplicates(inplace=True)

# 4. Standardize text columns (strip spaces, lowercase)
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().str.lower()

# 5. Convert date columns (if any)
# Example: if you have a column 'date'
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 6. Rename columns (lowercase, replace spaces with _)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 7. Check data types
print("\nData Types:\n", df.dtypes)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nFinal Shape:", df.shape)
print("✅ Data Cleaning Completed. Cleaned file saved as cleaned_dataset.csv")