import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#cities = pd.read_csv('../dotd/cities.csv')

election = pd.read_csv('kerg2.csv', sep=";")
parties = election[election.Gruppenart=='Partei']
all_votes = cum = parties.Anzahl.sum()
cum = parties.groupby('Gruppenname').Anzahl.sum()/all_votes 
party_names =  parties.Gruppenname.unique()

selection = []
print(party_names)
cum.plot(title='Bundestag 2025', color=['blue', 'green', 'black', '#000011', 'pink', 'red', '#232323'], kind='bar')


#plt.show()
print(cum.head())

# exit()

# all = election['Gültige Stimmen'].sum()
# print(all)
# elected = election.groupby('Gewählt')['Gültige Stimmen'].sum()/all
# # elected['percentage'] = election.groupby('Gewählt')['Gültige Stimmen'].sum()/all
# print(elected)


# plt.style.use('bmh')


#elected.plot(title='Bundestag 2025', color=['blue', 'green', 'black', '#000011', 'pink', 'red', '#232323'], kind='bar')


#plt.show()