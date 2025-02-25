#!/usr/bin/env python3
# datascience/cities_play
#
# SUBJECT: Playground for Pandas' DataFrame with cities datasets
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-02-24


# https://public.opendatasoft.com/explore/dataset/geonames-all-cities-with-a-population-1000/table/?disjunctive.cou_name_en&sort=name&refine.cou_name_en=France
import pandas as pd

file = "cities.de.json"


data = pd.read_json(file)
custom = data[["name", "population", "coordinates"]]
sorted = custom.sort_values("population", ascending = False)
# data.set_index("name", inplace = True)


print(data.head())
# print(data[['label_en', 'coordinates']].head())

# sorted.to_csv('foo.csv', index=False) #  save without index 