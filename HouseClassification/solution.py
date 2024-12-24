import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from category_encoders import TargetEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Stage 1/6: Import & explore
df = pd.read_csv('../Data/house_class.csv')

print(df.shape[0])
print(df.shape[1])
print(df.isnull().values.any())
print(df.Room.max())
print(df.Area.mean().round(1))
print(df.Zip_loc.nunique())

# Stage 2/6: Split the data
X = df[['Area', 'Room', 'Lon', 'Lat', 'Zip_area', 'Zip_loc']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=X.Zip_loc.values, random_state=1)

print(X_train.Zip_loc.value_counts().to_dict())

# Stage 3/6: One-hot encode the data
def one_hot(X_train, X_test):
    enc = OneHotEncoder(drop='first')
    enc.fit_transform(X_train[['Zip_area', 'Zip_loc', 'Room']])

    X_train_transformed = pd.DataFrame(
        enc.transform(X_train[['Zip_area', 'Zip_loc', 'Room']]).toarray(),
        index=X_train.index)
    X_train_transformed.columns = X_train_transformed.columns.astype(str)

    X_test_transformed = pd.DataFrame(
        enc.transform(X_test[['Zip_area', 'Zip_loc', 'Room']]).toarray(),
        index=X_test.index)
    X_test_transformed.columns = X_test_transformed.columns.astype(str)

    X_train_final = X_train[['Area', 'Lon', 'Lat']].join(X_train_transformed)
    X_test_final = X_test[['Area', 'Lon', 'Lat']].join(X_test_transformed)

    return X_train_final, X_test_final

def decision_tree(X_train, X_test, y_train):
    model = DecisionTreeClassifier(
        criterion='entropy',
        max_features=3,
        splitter='best',
        max_depth=6,
        min_samples_split=4,
        random_state=3)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return y_pred

def model_score(X_train, X_test, y_train, y_test):
    y_pred = decision_tree(X_train, X_test, y_train)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

X_train_onehot, X_test_onehot = one_hot(X_train, X_test)

# Stage 4/6:Ordinal encoder
def ordinal_enc(X_train, X_test):
    ordinal_enc = OrdinalEncoder()
    ordinal_enc.fit_transform(X_train[['Zip_area', 'Zip_loc', 'Room']])

    X_train_transformed = pd.DataFrame(
        ordinal_enc.transform(X_train[['Zip_area', 'Zip_loc', 'Room']]),
        index=X_train.index)
    X_train_transformed.columns = X_train_transformed.columns.astype(str)

    X_test_transformed = pd.DataFrame(
        ordinal_enc.transform(X_test[['Zip_area', 'Zip_loc', 'Room']]),
        index=X_test.index)
    X_test_transformed.columns = X_test_transformed.columns.astype(str)

    X_train_final = X_train[['Area', 'Lon', 'Lat']].join(X_train_transformed)
    X_test_final = X_test[['Area', 'Lon', 'Lat']].join(X_test_transformed)

    return X_train_final, X_test_final

X_train_ordinal, X_test_ordinal = ordinal_enc(X_train, X_test)


# Stage 5/6: Target encoder
def target_enc(X_train, X_test):
    target_enc = TargetEncoder(cols=['Zip_area', 'Room', 'Zip_loc'])
    target_enc.fit(X_train, y_train)

    X_train_transformed = pd.DataFrame(
        target_enc.transform(X_train),
        columns=X_train.columns,
        index=X_train.index)

    X_test_transformed = pd.DataFrame(
        target_enc.transform(X_test),
        columns=X_test.columns,
        index=X_test.index)

    return X_train_transformed, X_test_transformed

X_train_target, X_test_target = target_enc(X_train, X_test)

# Stage 6/6: Performance comparison
onehot_report = classification_report(y_test,
                                      decision_tree(X_train_onehot, X_test_onehot, y_train),
                                      output_dict=True)
onehot_macro_avg_f1 = round(onehot_report['macro avg']['f1-score'], 2)
print(f'OneHotEncoder:{onehot_macro_avg_f1}')

ordinal_report = classification_report(y_test,
                                       decision_tree(X_train_ordinal, X_test_ordinal, y_train),
                                       output_dict=True)
ordinal_macro_avg_f1 = round(ordinal_report['macro avg']['f1-score'], 2)
print(f'OrdinalEncoder:{ordinal_macro_avg_f1}')

target_report = classification_report(y_test,
                                      decision_tree(X_train_target, X_test_target, y_train),
                                      output_dict=True)
target_macro_avg_f1 = round(target_report['macro avg']['f1-score'], 2)
print(f'TargetEncoder:{target_macro_avg_f1}')