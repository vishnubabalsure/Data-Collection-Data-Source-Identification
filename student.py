import pandas as pd

# Load dataset
df = pd.read_csv("student_data.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
