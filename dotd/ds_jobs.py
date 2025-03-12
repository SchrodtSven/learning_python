import pandas as pd

df = pd.read_csv('data_science_job.csv')


print(df.experience.value_counts(dropna=False))