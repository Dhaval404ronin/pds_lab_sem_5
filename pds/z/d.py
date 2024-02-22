import pandas as pd

df = pd.read_csv("D:\F\pds\sample.csv",delimiter=',')

print(df)
import pandas as pd

print("First few rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("DataFrame information:")
print(df.info())
