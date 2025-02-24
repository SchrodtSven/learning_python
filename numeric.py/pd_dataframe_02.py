import pandas as pd

series_a = pd.DataFrame({'names': ['Peter', 'Mary Jane', 'Gwendolin', 'Betty'],
                       'rank': [8.2, 10.0, 9.9, 8.0]}, 
                       index = ['K1', 'K2', 'K3', 'K4'])
series_b = pd.DataFrame({'alias': ['friendly neighbourhood spider', 'Jackpot', 'Gwenom', 'Molten Girl'],
                       'power': [100.0, 98.1, 99.9, 78.4]}, 
                       index = ['K1', 'K2', 'K3', 'K4'])

series_nemesis = pd.DataFrame({'entity': ['Norman', 'Aunt', 'Father', 'Brother']})
print(series_nemesis)
series_joined = series_a.join(series_b, how='inner')
print(series_joined)


# join -> using indeces
# merge -> linking on 'on=...' attribute
