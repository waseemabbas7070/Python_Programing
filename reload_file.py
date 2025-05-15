import pandas as pd         # Importing pandas
import openpyxl             # (Optional) Explicitly importing openpyxl
df = pd.read_excel('data.xlsx', engine='openpyxl')  # Reading Excel file with specified engine
print(df)                   # Displaying the DataFrame
