#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

# Load the car dataset
car = pd.read_csv(r"/Users/user/Documents/Datasets for Practice/Cars Data1.csv")

# Display the first few rows of the dataset
print(car.head())

# Get the shape of the dataset
print("Dataset Shape:", car.shape)

# Handling missing values: Fill missing values in the 'Cylinders' column with its mean
car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)

# Display the dataset after handling missing values
print("\nDataset after handling missing values:")
print(car)

# Check for any remaining null values in the dataset
print("\nNull value count for each column:")
print(car.isnull().sum())

# Count the number of different car makes in the dataset
print("\nCar Makes and their Counts:")
print(car['Make'].value_counts())

# Show records where the 'Origin' is either 'Asia' or 'Europe'
print("\nRecords with 'Origin' as 'Asia' or 'Europe':")
print(car[car['Origin'].isin(['Asia', 'Europe'])])

# Remove records where the 'Weight' is above 4000
print("\nRecords with 'Weight' not above 4000:")
print(car[~(car["Weight"] > 4000)])

# Increase all values in the 'MPG_City' column by 3
car['MPG_City'] = car['MPG_City'].apply(lambda x: x + 3)

# Display the dataset after modifying 'MPG_City' values
print("\nDataset after increasing 'MPG_City' values by 3:")
print(car)





