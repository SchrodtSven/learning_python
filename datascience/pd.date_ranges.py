import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
# datetime_series = pd.Series(

#     pd.date_range("2000-01-01", periods=12, freq="MS")

# )

# print(datetime_series)

# df = pd.DataFrame(

#     {

#         'SepalLength': [6.5, 7.7, 5.1, 5.8, 7.6, 5.0, 5.4, 4.6, 6.7, 4.6],
#         'SepalWidth': [3.0, 3.8, 3.8, 2.7, 3.0, 2.3, 3.0, 3.2, 3.3, 3.6],
#         'PetalLength': [5.5, 6.7, 1.9, 5.1, 6.6, 3.3, 4.5, 1.4, 5.7, 1.0],
#         'PetalWidth': [1.8, 2.2, 0.4, 1.9, 2.1, 1.0, 1.5, 0.2, 2.1, 0.2],
#         'Category': [
#             'virginica',
#             'virginica',
#             'setosa'
#             'virginica',
#             'virginica',
#             'versicolor',
#             'versicolor',
#             'setosa',
#             'virginica',
#             'setosa'
#         ]
#     }
# )

# pd.plotting.radviz(df, 'Category')  
#s = pd.Series(np.random.uniform(size=100))

#pd.plotting.bootstrap_plot(s)  




#df = pd.read_csv('iris.csv')
#pd.plotting.parallel_coordinates(df, 'Name', color=('#556270', '#4ECDC4', '#C7F464', 'red', 'orange', 'blue'))

df = pd.DataFrame(np.random.randn(10, 3),

                  columns=['Col1', 'Col2', 'Col3'])

df['X'] = pd.Series(['A', 'A', 'A', 'A', 'A',

                     'B', 'B', 'B', 'B', 'B'])

df['Y'] = pd.Series(['A', 'B', 'A', 'B', 'A',

                     'B', 'A', 'B', 'A', 'B'])

boxplot = df.boxplot(column=['Col1', 'Col2'], by=['X', 'Y'])

plt.show()