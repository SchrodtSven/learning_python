import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

election = pd.read_csv('kerg2.csv', sep=";")
parties = election[election.Gruppenart=='Partei']
all_votes = cum = parties.Anzahl.sum()

# party_names =  parties.Gruppenname.unique()
party_names = ['SPD', 'CDU', 'GRÜNE', 'FDP', 'AfD', 'CSU', 'Die, Linke', 'FREIE, WÄHLER', 'Tierschutzpartei', 'dieBasis', 'Die, PARTEI', 'Team, Todenhöfer', 
               'PIRATEN', 'Volt', 'ÖDP', 'SSW', 'Verjüngungsforschung', 'PdH', 'Bündnis, C', 'BP', 'MLPD', 'MENSCHLICHE, WELT', 'PdF', 'SGP', 'BüSo', 
               'BÜNDNIS, DEUTSCHLAND', 'BSW', 'MERA25', 'WerteUnion']

selection = ['SPD', 'CDU', 'GRÜNE', 'FDP', 'AfD', 'CSU', 'Die, Linke', 'BSW']


cum = parties[parties.Gruppenname.isin(selection)].groupby('Gruppenname').Anzahl.sum()/all_votes 
print(cum)
cum.plot(title='Bundestag 2025', color=['#232323', '#49759c', '#6ba353', '#f075e6', '#7bc8f6', '#475f94', '#f5bf03', '#fffeb6', '#fffd74', '#895b7b', '#436bad', '#d0c101', '#c6f808', '#f43605', '#02c14d', '#b25f03', '#2a7e19', '#490648'], kind='pie')
plt.style.use('bmh')
plt.show()


exit()

#.groupby('Gruppenname').Anzahl.sum()/all_votes 


#print(cum)

# exit()

# all = election['Gültige Stimmen'].sum()
# print(all)
# elected = election.groupby('Gewählt')['Gültige Stimmen'].sum()/all
# # elected['percentage'] = election.groupby('Gewählt')['Gültige Stimmen'].sum()/all
# print(elected)


# 


#elected.plot(title='Bundestag 2025', color=['blue', 'green', 'black', '#000011', 'pink', 'red', '#232323'], kind='bar')


#plt.show()