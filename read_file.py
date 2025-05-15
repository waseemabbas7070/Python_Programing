import pandas as pd
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [28, 24, 35, 32],
    'city': ['New York', 'Paris', 'Berlin', 'London']

}

df = pd.DataFrame(data)  # Creating a DataFrame
df.to_excel('data.xlsx', index=False)  # Saving DataFrame to an Excel file
# Reading the Excel file
df = pd.read_excel('data.xlsx')  # Reading the Excel file
print(df)  # Displaying the DataFrame
# The code creates a DataFrame with sample data, saves it to an Excel file, and then reads the file back into a DataFrame, displaying the contents. 
# The code creates a DataFrame with sample data, saves it to an Excel file, and then reads the file
# back into a DataFrame, displaying the contents.
# The code creates a DataFrame with sample data, saves it to an Excel file, and then reads the file
# back into a DataFrame, displaying the contents.

