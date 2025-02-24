#!/usr/bin/env python3
# datasciencecities_play
# 
# SUBJECT: Playground for Pandas' DataFrame with cities datasets
# AUTHOR Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-01-03


# https://public.opendatasoft.com/explore/dataset/geonames-all-cities-with-a-population-1000/table/?disjunctive.cou_name_en&sort=name&refine.cou_name_en=France
import pandas as pd

file = 'cities.de.json'


data = pd.read_json(file)
custom = data[['name', 'population']]
sorted = custom.sort_values('population', ascending=False)
print(sorted.head(23))