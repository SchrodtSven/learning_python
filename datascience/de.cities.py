import pandas as pd

file = 'geonames-all-cities-with-a-population-1000.csv'
# geonames-all-cities-with-a-population-1000.csv
data = pd.read_csv(file)

print(data.head())