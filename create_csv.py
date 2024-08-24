import csv

# Data to be written to the CSV file
data = [
    ["col1", "col2", "col3"],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [4, 7, 10],
    [5, 8, 11]
]

# Create and write to the CSV file
with open('test_file.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'test_file.csv' created successfully.")