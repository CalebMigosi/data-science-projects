import pandas as pd

# Read Train CSV File
train_data = pd.read_csv("data/train.csv", sep = ",")

def find_percentage_of_existing_data(col_name):
    # Filter out rows with valid cabin numbers
    train_data_filter = train_data[col_name].apply(lambda x: False if pd.isnull(x) else True)
    filtered_train_data_by_cabin = train_data[train_data_filter]

    return filtered_train_data_by_cabin

# Find the percentage of Cabin columns
cabin_dataframe = find_percentage_of_existing_data("Cabin")
fare_dataframe = find_percentage_of_existing_data("Fare")

# Find the cabin number based on the class
print(sum(cabin_dataframe['Pclass'] == 1)/204)
