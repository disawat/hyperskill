# Project: Salary Predicition

## Stage 1/5: Linear regression with one independent variable
In the first stage, let's start with the simplest linear model — it will include salary as a dependent variable and the player's rating as the only predictor. Your goal is to fit such a model, find its coefficients and calculate the MAPE (mean average percentage error).
1. Load the DataFrame using the pandas.read_csv method;
2. Make X a DataFrame with a predictor rating and y a series with a target salary;
3. Split predictor and target into training and test sets. Use test_size=0.3 and random_state=100 parameters — they guarantee that the results will be as expected;
4. Fit the linear regression model with the following formula on the training data: salary∼rating.
5. Predict a salary with the fitted model on test data and calculate the MAPE.

## Stage 2/5: Linear regression with predictor transformation
On the scatterplot of rating vs salary, you may have noticed that the relationship between these two variables seems to be different from linear and looks like a polynomial function. Let's try to raise the rating by several degrees and see whether it improves the score.
1. Raise predictor to the power of 2.
2. Fit the linear model of salary on rating, make predictions and calculate the MAPE;
3. Repeat steps for the power of 3 and 4.

## Stage 3/5: Linear regression with many independent variable
In the previous stages, you used only one independent variable. Now, your task is to include other variables into a model.
1. Make X a DataFrame with predictors and y a series with a target. To make X, drop target variable from the data. All other variables leave unchanged.
2. Split the predictors and target into training and test sets. Use test_size=0.3 and random_state=100 — they guarantee that the results will be the same as the test system expects.
3. Fit the model predicting salary based on all other variables.
4. Print the model coefficients separated by a comma.

## Stage 4/5: Test for multicollinearity and variables selection
If you have a linear regression with many variables, some of them may be correlated. This way, the performance of the model may decrease. A crucial step is to check the model for multicollinearity and exclude the variables with a strong correlation with other variables. Carry out this check, find the best model by removing the variables with high correlation, and return its MAPE score.
1. Calculate the correlation matrix for the numeric variables;
2. Find the variables where the correlation coefficient is greater than 0.2. Hint: there should be three of them.
3. Make X, a DataFrame with all the predictor variables, and y, a series with the target.
4. Split the predictors and the target into training and test sets. Use test_size=0.3 and random_state=100 — they guarantee that the results will be as expected.
5. Fit the linear models for salary prediction based on the subsets of other variables. The subsets are as follows:
- First, try to remove each of the three variables you've found in step 2.
- Second, remove each possible pair of these three variables.
For example, if you have found out that the highly correlated variables are a, b, and c, then first you fit a model where a is removed, then a model without b, and then the model without c. After this, you estimate the model without both a and b, then without both b and c, and last, without both a and c. As a result, you will have six models to choose the best from.

## Stage 5/5: Deal with negative predictions
A linear model may predict negative values. However, such values can be meaningless because the salary can't be negative. In this stage, handle negative predictions.
1. As predictors select those variables that gave the best metric in the previous stage. Make X a DataFrame with predictors and y a series with a target. To make X, drop target variable from the data.
2. Split predictors and the target into train and test parts. Use test_size=0.3 and random_state=100 — they guarantee that the results will be the same as the test system expects.
3. Fit the model that predicts salary based on all other variables;
4. Predict the salaries.
5. Try two techniques to deal with negative predictions:
- replace the negative values with 0;
- replace the negative values with the median of the training part of y.
6. Calculate the MAPE for every two options and print the best as a floating number rounded to five decimal places.