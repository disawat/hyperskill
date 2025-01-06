# Project: NBA Data Preprocessing

## Description
In this project, we will preprocess the data to prepare it for use in a machine learning model that predicts the salaries of NBA players.

## Stage 1/4: It starts with a clean dataset
In this first stage, create a function called clean_data that takes the path to the dataset as a parameter. The function must:
1. Load a DataFrame from the location specified in the path parameter;
2. Parse the b_day and draft_year features as datetime objects;
3. Replace the missing values in team feature with "No Team";
4. Take the height feature in meters, the height feature contains metric and customary units;
5. Take the weight feature in kg, the weight feature contains metric and customary units;
6. Remove the extraneous $ character from the salary feature;
7. Parse the height, weight, and salary features as floats;
8. Categorize the country feature as "USA" and "Not-USA";
9. Replace the cells containing "Undrafted" in the draft_round feature with the string "0";
10. Return the modified DataFrame.

## Stage 2/4: Engineer to win
In this stage, you will build thefeature_data function with the output of the clean_data function. Inside the feature_data function:
1. The input parameter is the returned DataFrame from the clean_data function from the previous stage;
2. Get the unique values in the version column of the DataFrame you got from clean_data as a year (2020, for example) and parse as a datetime object;
3. Engineer the age feature by subtracting b_day column from version. Calculate the value as year;
4. Engineer the experience feature by subtracting draft_year column from version. Calculate the value as year;
5. Engineer the bmi (body mass index) feature from weight (w) and height (h) columns. The formula is bmi = w/h**2;
6. Drop the version, b_day, draft_year, weight, and height columns;
7. Remove the high cardinality features;
8. Return the modified DataFrame.

## Stage 3/4: I'm multicollinearity
In this stage, you will build the multicol_data function given the DataFrame preprocessed by feature_data function from the previous stage. Inside the multicol_data function:
1. The input parameter is the returned DataFrame from the feature_data function. It contains features and the target variable, which is salary.
2. Check your data for multicollinearity using the Pearson correlation coefficient. First, calculate the correlation matrix for the numerical features in X and take note of both features with a correlation coefficient above 0.5 or below -0.5.
3. Take both features and find their correlation coefficients with the target variable — salary.
4. Drop the feature that has the lowest correlation coefficient with the target variable.
5. Return the modified DataFrame.

## Stage 4/4: Transform to high quality
In this stage, implement the data preprocessing pipeline inside the transform_data function. Your function must:
1. As the input parameter, take the DataFrame returned from multicol_data function, which you implemented in the previous stage;
2. Transform numerical features in the DataFrame it got from multicol_data using StandardScaler;
3. Transform nominal categorical variables in the DataFrame using OneHotEncoder; Use OneHotEncoder's categories_ attribute to get the returned array feature names.
Bear in mind that the default setting of OneHotEncoder's sparse_output parameter is True. Set it to False or use the .toarray() function to transform encoded data before creating the DataFrame.
4. Concatenate the transformed numerical and categorical features in the following order: numerical features, then nominal categorical features;
5. Return two objects: X, where all the features are stored, and y with the target variable.
