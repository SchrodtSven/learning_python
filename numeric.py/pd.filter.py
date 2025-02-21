# pd.filter.py
#
# SUBJECT: filtering data with Pandas
# AUTHOR Sven Schrodt
# SEE: https://raw.githubusercontent.com/JackyP/testing/master/datasets/
import pandas as pd
df = pd.read_csv("nycflights.csv", usecols=range(1,17))
# year  month  day  dep_time  dep_delay  arr_time  arr_delay carrier tailnum  flight origin dest  air_time  distance  hour  minute

# print(df.head())
# newdf = df[(df.origin == "JFK") & (df.carrier == "B6")]
# print(newdf)

foo_slice = df[(df['distance']>900) & (df['dest'].isin(['OMA', 'CRW', 'OAK', 'SMF']))]
# origin, dest = df['origin'].unique(), df['dest'].unique()
# print(origin, dest)


print(foo_slice.select_dtypes('float'))