# Importiere, was du so fürs Leben brauchst ;)
import seaborn as sns
import pandas as pd
 
def calc_sal_lvl(income: int):
    if income < 30000:
        return 'low income'
         
    if income > 30000 and income < 100000:
        return 'middle income'
    if income >= 100000:
        return 'high income'
    
data = pd.read_csv('ds_jobs_fr_de.csv')
data['salary_lvl'] = data['salary'].map(calc_sal_lvl)
print(data.head(23))


