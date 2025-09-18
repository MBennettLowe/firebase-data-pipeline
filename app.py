# Extracting data from CSV flat file. Flat file name - fake_civic_polling_data

# Import pandas
import pandas as pd;

# Read the dataset into memory, and take a look at the first few rows (store as apps)
apps = pd.read_csv("fake_civic_polling_data.csv")

# Print out the head of the DataFrame
print(apps.head())
#print(apps)

# Perform some basic checks (column names, number of records, types, etc)