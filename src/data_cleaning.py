import pandas as pd
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Build file paths safely
raw_data_path = BASE_DIR / "data" / "raw" / "netflix_titles.csv"
processed_data_path = BASE_DIR / "data" / "processed" / "netflix_cleaned.csv"

# Load dataset
df = pd.read_csv(raw_data_path)

# Cleaning
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['director'] = df['director'].fillna('Not Available')
df['cast'] = df['cast'].fillna('Not Available')

# Save cleaned data
df.to_csv(processed_data_path, index=False)

print("✅ Cleaned data saved successfully!")

