import pandas as pd

# Load the dataset
file_path = "C:/Users/Vishal M/InnobyteIntern/dataset.csv"  # Update with your dataset file path
df = pd.read_csv(file_path)

# Preview the dataset
print(df.head())
print(df.info())  # Check column data types and null values

# Drop irrelevant and entirely null columns
df.drop(columns=['index', 'New', 'PendingS'], inplace=True)
# Inspect the unique formats in the 'Date' column
print(df['Date'].unique()[:10])

# Clean and preprocess the 'Date' column
df['Date'] = df['Date'].str.strip()  # Remove extra spaces
df['Date'] = df['Date'].str[:8]      # Remove unexpected extra characters

# Convert to datetime with error handling
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y', errors='coerce')

# Check and handle invalid dates
invalid_dates = df[df['Date'].isna()]
print("Invalid dates:")
print(invalid_dates)

# Drop rows with invalid dates
df.dropna(subset=['Date'], inplace=True)

# Verify the cleaned column
print(df['Date'].head())


# Convert postal code to string
df['ship-postal-code'] = df['ship-postal-code'].astype(str)

df['fulfilled-by'] = df['fulfilled-by'].fillna('Unknown')
df['currency'] = df['currency'].fillna('INR')


# Drop rows with missing geographical information
df.dropna(subset=['ship-city', 'ship-state', 'ship-country'], inplace=True)

df['Qty'] = df['Qty'].astype('int32')
df['ship-country'] = df['ship-country'].astype('category')


# Check for duplicates and remove them
df.drop_duplicates(inplace=True)

# Verify the cleaned dataset
print(df.info())
print(df.head())


df.to_csv(r'C:\Users\Vishal M\InnobyteIntern\cleaned_data.csv', index=False)

print("Cleaned data saved to cleaned_data.csv")
