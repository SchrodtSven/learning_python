import seaborn as sns
import pandas as pd
def calc_sal_lvl(income: int):
    if income < 30000:
        return 'low income'
         
    if income > 30000 and income < 80000:
        return 'middle income'
    if income >= 80000:
        return 'high income'
    
data = pd.read_csv('data_science_salaries.csv')
#data.info()
# print(data.groupby('employee_residence').head(5))

# print(type(data['salary']))
# <class 'pandas.core.series.Series'>
# exit()

# for x in data.salary:
     
#     print(calc_sal_lvl(x))

data['salary_level'] = data['salary'].map(calc_sal_lvl)

# Hint: Pandas does NOT have DataFrame.map() - only Series.map(), so if you need to access multiple columns 
# in your mapping function - you can use DataFrame.apply().
# data['foo'] = data.apply(lamba x: my_function(data.x))

print(data.tail(23))

#print(data)
fr_de = data[data['company_location'].isin(['Germany', 'France'])].sort_values('salary')
fr_de.to_csv('data_jobs.csv')

