import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from PIL import Image

df = sns.load_dataset('titanic')

#print(df.head())

df2 = pd.read_csv('titanic_new.csv')
print(len(df2))

print(df2.describe())

#print(df2.Cabin.value_counts(dropna=False))

# sib = df.groupby(['class'], observed=False).fare.mean()
# print(df.deck.value_counts(dropna=False))
# exit()
# sib.plot(kind='bar', stacked=True)
# plt.grid(visible=True, color='green')
# plt.show()