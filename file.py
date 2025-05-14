import csv

# Define data
data = [
    ['name', 'Age', 'City'],
    ['Waseem', 24, 'Lahore'],
    ['Nadeed', 20, 'Sahiwal']
]

# Write to data.csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # <-- FIXED here

# Print specific item
print(data)  # Output: Age

# Read and print from info.csv
# with open('info.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
