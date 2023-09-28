import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
data_frame = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(data_frame)

# Accessing Columns
print("\nAccessing Columns:")
print(data_frame['Name'])
print(data_frame.Age)

# Getting the shape of the DataFrame
print("\nShape of DataFrame:")
print(data_frame.shape)

# Getting summary statistics of the numeric columns
print("\nSummary Statistics:")
print(data_frame.describe())

# Filtering Data
filtered_df = data_frame[data_frame['Age'] > 30]
print("\nFiltered DataFrame:")
print(filtered_df)

# Sorting Data
sorted_df = data_frame.sort_values(by='Age')
print("\nSorted DataFrame:")
print(sorted_df)

# Adding a New Column
data_frame['Country'] = ['USA', 'Canada', 'UK']
print("\nDataFrame with New Column:")
print(data_frame)

# Grouping and Aggregating Data
grouped = data_frame.groupby('Country')['Age'].mean()
print("\nGrouped and Aggregated Data:")
print(grouped)
