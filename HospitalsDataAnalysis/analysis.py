import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)

# Stage 1/5: Upload the data
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

# Stage 2/5: Merge them!
prenatal.columns = general.columns
sports.columns = general.columns

df = pd.concat([general, prenatal, sports], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)

# Stage 3/5: Improve your dataset
df.dropna(how='all', inplace=True)

def correct_gender(gender):
    if gender in ['female', 'woman']:
        return 'f'
    elif gender in ['male', 'man']:
        return 'm'
    elif pd.isna(gender):
        return 'f'
    else:
        return gender

df['gender'] = df['gender'].apply(correct_gender)

fill_columns = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
df[fill_columns] = df[fill_columns].fillna(0)

# Stage 4/5: The statistics
pd.reset_option('display.max_columns')

count_patients = df['hospital'].value_counts()
highest_patients = count_patients.idxmax()

general_hospital = df[df['hospital'] == 'general']
general_stomach = (general_hospital['diagnosis'] == 'stomach').mean()

sports_hospital = df[df['hospital'] == 'sports']
sports_dislocation = (sports_hospital['diagnosis'] == 'dislocation').mean()

median_age_general = general_hospital['age'].median()
median_age_sports = sports_hospital['age'].median()
median_age_diff = abs(median_age_general - median_age_sports)

bt_counts = pd.pivot_table(df[df['blood_test'] == 't'], values='blood_test', index='hospital', aggfunc='count')
most_bt_hospital = bt_counts.idxmax()[0]
most_bt_count = bt_counts.max()[0]

print(f'The answer to the 1st question is {highest_patients}')
print(f'The answer to the 2nd question is {general_stomach:.3f}')
print(f'The answer to the 3rd question is {sports_dislocation:.3f}')
print(f'The answer to the 4th question is {median_age_diff}')
print(f'The answer to the 5th question is {most_bt_hospital}, {most_bt_count} blood tests')

# Stage 5/5: Visualize it!
# 1. Most common age range among all hospitals
age_bins = [0, 15, 35, 55, 70, 80]
age_labels = ['0-15', '15-35', '35-55', '55-70', '70-80']
df['age_range'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

most_common_age = df['age_range'].value_counts().idxmax()

plt.figure(figsize=(8, 5))
df['age_range'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Most Common Age Range of Patients")
plt.xlabel("Age Range")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()

# 2. Most common diagnosis among all hospitals
most_common_diag = df['diagnosis'].value_counts().idxmax()

plt.figure(figsize=(8, 5))
df['diagnosis'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Most Common Diagnosis Among Patients")
plt.ylabel("")  # Remove y-label for a cleaner look
plt.show()

# 3. Violin plot of height distribution by hospitals
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x='hospital', y='height', palette="muted", inner='quartile')
plt.title("Height Distribution by Hospital")
plt.xlabel("Hospital")
plt.ylabel("Height")
plt.show()

print(f'The answer to the 1st question: {most_common_age}')
print(f'The answer to the 2nd question: {most_common_diag}')
print(f'The answer to the 3rd question: The gap in values is likely due to differences in patient demographics across hospitals. \
The two peaks may correspond to common patients (shorter heights) and athletes (taller heights).')
