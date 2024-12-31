import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error as mape
from itertools import combinations

df = pd.read_csv('../Data/data.csv')

# Stage 1/5: Linear regression with one independent variable
X = df[['rating']]
y = df['salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

model1 = LinearRegression()
model1.fit(X_train, y_train)

y_pred = model1.predict(X_test)
mape1 = mape(y_test, y_pred)

print(f'{model1.intercept_:.5f} {model1.coef_[0]:.5f} {mape1:.5f}')

# Stage 2/5: Linear regression with predictor transformation
best_mape = float('inf')
best_power = int()
for power in range(1, 5):
    X_train_poly = X_train ** power
    X_test_poly = X_test ** power

    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    y_pred = model.predict(X_test_poly)

    mape_poly = mape(y_test, y_pred)

    if mape_poly < best_mape:
        best_mape = mape_poly
        best_power = power

print(f'{best_power}, {best_mape:.5f}')

# Stage 3/5: Linear regression with many independent variable
X = df.drop(columns=['salary'])
y = df['salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

model = LinearRegression()
model.fit(X_train, y_train)

print(", ".join(map(str, model.coef_)))

# Stage 4/5: Test for multicollinearity and variables selection
cm = df.drop(columns=['salary']).corr()
high_corr_vars = cm[cm['rating'].abs() > 0.2].index.tolist()

X = df.drop(columns=['salary'])
y = df['salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

best_mape = float('inf')
best_vars = []

# Removing individual variables
for var in high_corr_vars:
    X_train_subset = X_train.drop(columns=[var])
    X_test_subset = X_test.drop(columns=[var])

    model = LinearRegression()
    model.fit(X_train_subset, y_train)
    y_pred = model.predict(X_test_subset)

    mape_corr = mape(y_test, y_pred)
    if mape_corr < best_mape:
        best_mape = mape_corr
        best_vars = X_test_subset.columns.tolist()

# Removing pairs of variables
for var_pair in combinations(high_corr_vars, 2):
    X_train_subset = X_train.drop(columns=list(var_pair))
    X_test_subset = X_test.drop(columns=list(var_pair))

    model = LinearRegression()
    model.fit(X_train_subset, y_train)
    y_pred = model.predict(X_test_subset)

    mape_corr = mape(y_test, y_pred)
    if mape_corr < best_mape:
        best_mape = mape_corr
        best_vars = X_test_subset.columns.tolist()

print(f'{best_vars} {best_mape:.5f}')

# Stage 5/5: Deal with negative predictions
X = df[best_vars]
y = df['salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Option 1: Replace negative values with 0
y_pred_zero = [max(0, pred) for pred in y_pred]

# Option 2: Replace negative values with the median of the training target
y_median = y_train.median()
y_pred_median = [pred if pred >= 0 else y_median for pred in y_pred]

mape_zero = mape(y_test, y_pred_zero)
mape_median = mape(y_test, y_pred_median)

print(f'{min(mape_zero, mape_median):.5f}')
