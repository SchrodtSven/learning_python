import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
election = pd.read_csv('kerg2.csv', sep=";")
parties = election[election.Gruppenart=='Partei']
all_votes = cum = parties.Anzahl.sum()


print(matplotlib.style.available)
with plt.xkcd():
    # party_names =  parties.Gruppenname.unique()
    party_names = ['SPD', 'CDU', 'GRÜNE', 'FDP', 'AfD', 'CSU', 'Die, Linke', 'FREIE, WÄHLER', 'Tierschutzpartei', 'dieBasis', 'Die, PARTEI', 'Team, Todenhöfer', 
                'PIRATEN', 'Volt', 'ÖDP', 'SSW', 'Verjüngungsforschung', 'PdH', 'Bündnis, C', 'BP', 'MLPD', 'MENSCHLICHE, WELT', 'PdF', 'SGP', 'BüSo', 
                'BÜNDNIS, DEUTSCHLAND', 'BSW', 'MERA25', 'WerteUnion']


    selection = ['SPD', 'CDU', 'GRÜNE', 'FDP', 'AfD', 'CSU', 'Die, Linke', 'BSW']


    cum = parties[parties.Gruppenname.isin(selection)].groupby('Gruppenname').Anzahl.sum()/all_votes 
    #print(cum)
    cum.plot(title='Bundestag 2025', color=['#232323', '#49759c', '#6ba353', '#f075e6', '#7bc8f6', '#475f94', '#f5bf03', '#fffeb6', '#fffd74', '#895b7b', '#436bad', '#d0c101', '#c6f808', '#f43605', '#02c14d', '#b25f03', '#2a7e19', '#490648'], kind='pie')
    plt.style.use('bmh')
    
    
    
    plt.show()

# print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
