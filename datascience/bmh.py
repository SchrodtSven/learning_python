import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
cities = pd.read_csv('../dotd/cities.csv')
#'Unnamed: 0', 'geoname_id', 'name', 'ascii_name', 'alternate_names',
    #    'feature_class', 'feature_code', 'country_code', 'cou_name_en',
    #    'country_code_2', 'admin1_code', 'admin2_code', 'admin3_code',
    #    'admin4_code', 'population', 'elevation', 'dem', 'timezone',
    #    'modification_date', 'label_en', 'coordinates'],

#print(cities.head())
de_cit = cities[(cities.country_code == 'DE') & (cities.population >100_000)]
plt.style.use('bmh')
de_cit[['elevation', 'population']].plot();

plt.show()