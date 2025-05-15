import pandas as pd
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [28, 24, 35, 32],
    'city': ['New York', 'Paris', 'Berlin', 'London']

}

df = pd.DataFrame(data)  # Creating a DataFrame
df.to_excel('output.xlsx', index=False)  # Saving DataFrame to an Excel file


