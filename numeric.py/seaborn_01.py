# Import seaborn

# head | tail default 5 as in unix-like OSs
# 

import seaborn as sns
import seaborn.objects as so
#import matplotlib_inline as matplotlib
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
#flights.head()
#sns.relplot(data=flights, x="year", y="passengers", hue="month", kind="line")
#print(len(flights))
#plt.show()

# print(sns.get_dataset_names())
# 'anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 
# 'diamonds', 'dots', 'dowjones', 'exercise', 'flights', 'fmri',  'geyser', 
# 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']
ds_name = 'titanic'
curr_ds = sns.load_dataset(ds_name)
# print(curr_ds.head()) # 8 <- 'Snowie'
print(curr_ds.loc[:20:2, ['sex', 'class']]) # 0...20 stepped by 2, only attributes('sex', 'class')
# print(curr_ds['sex'].unique())
# p = so.Plot(curr_ds)
# p.facet()

tl_age = curr_ds['age'].sum()
print(f'total sum of all ages:{tl_age}')

