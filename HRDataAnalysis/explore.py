import pandas as pd

# Stage 1/5: Load the data and modify the indexes
doa = pd.read_xml('../Data/A_office_data.xml')
dob = pd.read_xml('../Data/B_office_data.xml')
dhr = pd.read_xml('../Data/hr_data.xml')
doa['employee_id'] = 'A' + doa['employee_office_id'].astype(str)
doa.set_index('employee_id', inplace=True)
dob['employee_id'] = 'B' + dob['employee_office_id'].astype(str)
dob.set_index('employee_id', inplace=True)
dhr.set_index('employee_id', inplace=True)

# Stage 2/5: Merge everything
dof = pd.concat([doa, dob])
df = dof.merge(dhr, left_index=True, right_index=True, how='left', indicator=True)
df = df[df['_merge'] == 'both']
df.drop(columns=['employee_office_id', '_merge'], inplace=True)
df.sort_index(inplace=True)

# Stage 3/5: Get the insights
top_ten_departments = df.sort_values(by='average_monthly_hours', ascending=False)['Department'].head(10).tolist()
it_low_salary_projects = df[(df['Department'] == 'IT') & (df['salary'] == 'low')]['number_project'].sum()
employee_scores = df.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']].values.tolist()
print(top_ten_departments)
print(it_low_salary_projects)
print(employee_scores)

# Stage 4/5: Aggregate the data
def count_bigger_5(series):
    return (series > 5).sum()

metrics = df.groupby('left').agg({
    'number_project': ['median', count_bigger_5],
    'time_spend_company': ['mean', 'median'],
    'Work_accident': ['mean'],
    'last_evaluation': ['mean', 'std']
}).round(2)
print(metrics.to_dict())

# Stage 5/5: Draw up pivot tables
pvt1 = df.pivot_table(
    values='average_monthly_hours',
    index='Department',
    columns=['left', 'salary'],
    aggfunc='median')

filter_pvt1 = pvt1.loc[
    (pvt1[(0.0, 'high')] < pvt1[(0.0, 'medium')]) |
    (pvt1[(1.0, 'low')] < pvt1[(1.0, 'high')])]

pvt2 = df.pivot_table(
    values=['satisfaction_level', 'last_evaluation'],
    index='time_spend_company',
    columns='promotion_last_5years',
    aggfunc=['min', 'max', 'mean'])

filter_pvt2 = pvt2.loc[
    pvt2[('mean', 'last_evaluation', 0)] > pvt2[('mean', 'last_evaluation', 1)]]

print(filter_pvt1.round(2).to_dict())
print(filter_pvt2.round(2).to_dict())