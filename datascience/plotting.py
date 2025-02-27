import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dj = sns.load_dataset('dowjones')
dj.info()
dj.plot(x='Date', y='Price', color='red')
plt.xkcd()
plt.show()

