import pandas as pd
import matplotlib.pylab as plt

data = pd.read_csv('autoscout24-germany-dataset.csv')
price_per_year_model = data.groupby(['year', 'model']).price.mean()


price_per_year = data.groupby('year').price.mean()
print(price_per_year)

with plt.xkcd():
    price_per_year.plot(x = 'year', y = 'price', title = 'Ø-Preise nach Modell / Jahr', grid=True)

plt.show()