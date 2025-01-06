import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Stage 1/4: It starts with a clean dataset
def clean_data(path):
    df = pd.read_csv(path)

    df['b_day'] = pd.to_datetime(df['b_day'], format='%m/%d/%y')
    df['draft_year'] = pd.to_datetime(df['draft_year'], format='%Y')
    df.fillna({'team': 'No Team'}, inplace=True)
    df['height'] = df['height'].apply(lambda x: float(x.split('/')[-1].strip()))
    df['weight'] = df['weight'].apply(lambda x: float(x.split('/')[-1].strip().replace('kg.', '').strip()))
    df['salary'] = df['salary'].apply(lambda x: float(x.replace('$', '').replace(',', '')))
    df['country'] = df['country'].apply(lambda x: 'USA' if x == 'USA' else 'Not-USA')
    df['draft_round'] = df['draft_round'].replace('Undrafted', '0')

    return df

# Stage 2/4: Engineer to win
def feature_data(df):
    df['version'] = pd.to_datetime(df['version'].apply(lambda x: float(x.replace('NBA2k', '20'))), format='%Y')
    df['age'] = df['version'].dt.year - df['b_day'].dt.year
    df['experience'] = df['version'].dt.year - df['draft_year'].dt.year
    df['bmi'] = df['weight'] / (df['height'] ** 2)

    df.drop(columns=['version', 'b_day', 'draft_year', 'weight', 'height'], inplace=True)

    high_cardinality_features = [col for col in df.select_dtypes('object') if df[col].nunique() >= 50]
    df.drop(columns=high_cardinality_features, inplace=True)

    return df

# Stage 3/4: I'm multicollinearity
def multicol_data(df):
    corr_matrix = df.select_dtypes('number').drop(columns=['salary']).corr()

    high_corr_pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > 0.5:
                high_corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j]))

    to_drop = []
    for feature1, feature2 in high_corr_pairs:
        corr1 = df[feature1].corr(df['salary'])
        corr2 = df[feature2].corr(df['salary'])

        if abs(corr1) < abs(corr2):
            to_drop.append(feature1)
        else:
            to_drop.append(feature2)

    df = df.drop(columns=set(to_drop))

    return df

# Stage 4/4: Transform to high quality
def transform_data(df):
    num_feat_df = df.select_dtypes('number').drop(columns=['salary'])
    cat_feat_df = df.select_dtypes('object')

    scaler = StandardScaler()
    num_feat_scaled = scaler.fit_transform(num_feat_df)

    encoder = OneHotEncoder(sparse_output=False)
    cat_feat_encoded = encoder.fit_transform(cat_feat_df)
    cat_feat_cols = [value for feature_values in encoder.categories_ for value in feature_values]

    X_scaled = pd.DataFrame(num_feat_scaled, columns=num_feat_df.columns)
    X_encoded = pd.DataFrame(cat_feat_encoded, columns=cat_feat_cols)
    X = pd.concat([X_scaled, X_encoded], axis=1)

    y = df['salary']

    return X, y

path = '../Data/nba2k-full.csv'
df_cleaned = clean_data(path)
df_featured = feature_data(df_cleaned)
df = multicol_data(df_featured)
X, y = transform_data(df)

answer = {'shape': [X.shape, y.shape], 'features': list(X.columns)}
print(answer)