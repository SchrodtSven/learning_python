import pandas as pd

df = pd.read_csv('data_science_salaries.csv')
print(df.head())

print(df.company_location.value_counts())

print(df.company_location.mode())