import pandas as pd

file = 'cities.csv'

data = pd.read_csv(file)
# data.columns = ['Country_Code', 'City', 'Latitude', 'Longitude']
print(data['Country_Code'].unique())
# #print(type(data))
# # data.set_index(['Country_Code', 'Name', 'Latitude', 'Longitude'])
# # print(data.head())

# de = data[data['Country_Code'] == 'DE']
# de.to_json('de.cities.json')
# print(de.head())
# print(de.tail())

