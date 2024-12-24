# Project: House Classification

## Description
Before starting to work with your data, you need to explore it first. Luckily, your data is mostly preprocessed! The dataset contains information about houses for sale in the following columns:

Price — the price of the house. Class 0 stands for affordable housing with a price of less than 700000 euros, and class 1 stands for expensive housing with the price of more than 700000 euros;
Area — the area of the house;
Room — how many rooms in the house;
Lon — house longitude coordinates;
Lat — house latitude coordinates;
Zip_area — house location in the specific area of the Netherlands based on the zip code;
Zip_loc — house location in a specific Amsterdam area based on the zip code.

## Stage 1/6: Import & explore

1. Load the data into the pandas DataFrame;
2. Analyze the data and print the answers to the following questions:
- How many rows does the DataFrame have?
- How many columns does the DataFrame have?
- Are there any missing values in the DataFrame (True or False)?
- What is the maximum number of rooms across the houses in the dataset?
- What is the mean area of the houses in the dataset?
- How many unique values does column Zip_loc contain?

## Stage 2/6: Split the data

Continue to work with the data from the previous stage. To complete this stage:
1. Import train_test_split from scikit-learn;
2. Create two separate datasets:
- The X dataset for the following columns Area, Room, Lon, Lat, Zip_area, and Zip_loc;
- The y dataset for the Price target column;
3. Split the two datasets using the train_test_split function. The test data proportion is 30%. Set the stratify parameter to X['Zip_loc'].values, random_state to 1. Note that this will create a total of four separate datasets;
4. Print the value count dictionary of the Zip_loc column in the final training dataset.

## Stage 3/6: One-hot encode the data

Continue to work with the data from the previous stage. To complete this stage:
1. Import OneHotEncoder from sklearn.preprocessing;
2. Create the encoder and specify the drop='first' parameter to drop the first column, created by the encoder;
3. Fit the encoder to the training data using three categorical columns: Zip_area, Zip_loc, Room;
4. Transform the training and the test datasets with the fitted encoder. 
5. Return the transformed data to the dataset using the code below.
6. Use DecisionTreeClassifier from scikit-learn. Initialize the model with the following parameters: criterion='entropy', max_features=3, splitter='best', max_depth=6, min_samples_split=4, and random_state=3. Fit the model to the training data and predict the house prices on the test data;
7. Evaluate the model's accuracy using the accuracy_score function from sklearn.metrics;
8. Print the accuracy value.

## Stage 4/6:Ordinal encoder

Continue to work with the data from the previous stage. To complete this stage:
1. Import OrdinalEncoder from sklearn.preprocessing;
2. Create the encoder.
3. Fit the encoder to the training data using three categorical columns: Zip_area, Zip_loc, Room;
4. Transform the training and the test datasets with the fitted encoder;
5. Feed the transformed data back into the dataset in the same way as you did in the previous stage;
6. Initialize the DecisionTreeClassifier model with the same parameters as in the previous stage. Fit a model to the training data and predict the house prices on the test data;
7. Evaluate the model's accuracy using the accuracy_score function;
8. Print the accuracy value.

## Stage 5/6: Target encoder

Continue to work with the data from the previous stage. To complete this stage:
1. Make sure that you have the category_encoders library installed in your projects;
2. Import TargetEncoder from category_encoders;
3. Create one TargetEncoder encoder for three categorical columns in this sequence: Zip_area, Room and Zip_loc;
4. Fit the encoder to the training data;
5. Transform the training and the test datasets with the fitted encoder;
6. Initialize the DecisionTreeClassifier model with the same parameters as in the previous stages. Fit a model to the training data and predict the house prices on the test data;
7. Evaluate the model's accuracy using the accuracy_score function;
8. Print the accuracy value.

## Stage 6/6: Performance comparison

Continue to work with the data from the previous stage. To complete this project:
1.Use classification_report to evaluate the metrics of each of the three DecisionTreeClassifier models trained on data transformed with three different encoders;
2.For each of the models, print the transformer and F1 score macro average value. Round the result to two digits.