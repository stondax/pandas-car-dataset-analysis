### pandas-car-dataset-analysis

Car Dataset Analysis

This Python script performs a comprehensive analysis of a car dataset using the powerful pandas library. Let's take a closer look at each step and its purpose:

### Initial Data Exploration
The script prints the first five rows of the dataset using 'car.head()' to get a glimpse of its structure. This helps to understand the types of columns and the data they contain.

### Checking Dataset Shape
To get an overview of the dataset's size, 'car.shape' is used, displaying the number of rows and columns. In this case, the dataset contains 432 rows and 15 columns.

### Handling Missing Values
The script proceeds to identify and handle missing values in the dataset. By using 'car.isnull().sum()', it calculates the number of null values for each column. The column 'Cylinders' is found to have 6 missing values. These missing values are filled with the mean of the 'Cylinders' column using 'car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)'.

### Displaying Missing Value Updates
After filling the missing values, the dataset is displayed again to verify the changes. This helps ensure data integrity and reliability.

### Counting Car Makes
The script then performs a count of different car makes present in the dataset. Using 'car['Make'].value_counts()', it displays the number of occurrences for each car make, providing valuable insights into the dataset's distribution.

### Filtering Data Based on Origin
Next, the script filters the records based on the 'Origin' column. It displays all the records where the 'Origin' is either 'Asia' or 'Europe' using 'car[car['Origin'].isin(['Asia', 'Europe'])]'. This allows for specific analysis and comparisons among cars from these regions.

### Filtering Data Based on Weight
The script also filters the dataset to show records where the 'Weight' of the car is above 4000. Using 'car[car["Weight"] > 4000]', it displays these records. Additionally, it displays the records where the weight is not above 4000 using 'car[~(car["Weight"] > 4000)]'.

### Modifying Data - Increasing 'MPG_City' Values
The script increases all the values in the 'MPG_City' column by 3 using a lambda function and 'car['MPG_City'] = car['MPG_City'].apply(lambda x: x + 3)'. This modification can be useful for various analysis and comparisons related to fuel efficiency.

### Final Display of Modified Dataset
Finally, the script displays the modified dataset, showing the changes made to the 'MPG_City' column.

By following this comprehensive analysis, users can gain valuable insights into the car dataset, such as missing data handling, distribution of car makes, filtering data based on specific criteria, and making data modifications as needed.
