# Project: Data Analysis for Hospitals

## Description
Imagine you are a data scientist and you're currently working with the data for local hospitals. You have several files with information about patients from different districts. Sometimes, the data is split into many datasets or may contain empty or invalid values. The first step is to preprocess the data before the analysis: merge the files into one, delete empty or incorrect rows, fill the missing values, and so on.

## Stage 1/5: Upload the data
The input is 3 CSV files, test/general.csv, test/prenatal.csv, and test/sports.csv.
You need to upload the data from the hidden test directory of the project for further processing.

## Stage 2/5: Merge them!
1. Change the column names. All column names in the sports and prenatal tables must match the column names in the general table
2. Merge the DataFrames into one. Use the ignore_index=True parameter and the following order: general, prenatal, sports
3. Delete the Unnamed: 0 column

## Stage 3/5: Improve your dataset
1. Delete all the empty rows
2. Correct all the gender column values to f and m respectively
3. Replace the NaN values in the gender column of the prenatal hospital with f
4. Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeros

## Stage 4/5: The statistics
Answer the following questions and output the answers in the specified format.
1. Which hospital has the highest number of patients?
2. What share of the patients in the general hospital suffers from stomach-related issues? Round the result to the third decimal place.
3. What share of the patients in the sports hospital suffers from dislocation-related issues? Round the result to the third decimal place.
4. What is the difference in the median ages of the patients in the general and sports hospitals?
5. After data processing at the previous stages, the blood_test column has three values: t = a blood test was taken, f = a blood test wasn't taken, and 0 = there is no information. In which hospital the blood test was taken the most often (there is the biggest number of t in the blood_test column among all the hospitals)? How many blood tests were taken?

## Stage 5/5: Visualize it!
In the last stage, create data visualization to answer the following questions:
1. What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.
2. What is the most common diagnosis among patients in all hospitals? Create a pie chart.
3. Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values?