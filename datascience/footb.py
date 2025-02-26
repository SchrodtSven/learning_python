import pandas as pd

data = pd.read_csv('football_eng_24245.csv')
print(data.head())

print(data.HomeTeam.unique())
