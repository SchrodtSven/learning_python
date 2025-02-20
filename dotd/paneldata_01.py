import numpy as np
import pandas as pd

my_series = pd.Series(['Sven', 'is','hunting','Doc Ock', 'and', 'Venom'])

print(my_series, len(my_series))


cities = ['Kolkata', 'Chicago', 'Toronto', 'Lisbon']

populations = [14.85, 2.71, 2.93, 0.51]

city_series = pd.Series(populations, index=cities)
print(city_series)
print(city_series.index)

di = city_series.to_dict()
print(type(di), di)

pd_dict = pd.Series(di)
print(pd_dict)

# Sl@nG -> Programmiersprache
