import pandas as pd
import matplotlib.pyplot as plt

# URL to the Excel file
url = "https://github.com/chris1610/pbpython/blob/master/data/sample%20salesv3.xlsx?raw=true"

# Read the Excel file
df = pd.read_excel(url)

# You can view the first few rows of the dataset if needed
# print(df.head())

# Assuming the dataset has columns like "date" and "sales", you can create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(df["date"], df["sales"])
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Data from Excel File")
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

# Display the plot
plt.tight_layout()
plt.show()
