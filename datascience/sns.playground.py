#!/usr/bin/env python3
# datascience/cities_play
#
# SUBJECT: Playground for Seaborn's stuff
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-02-26
import numpy as np
import seaborn as sns

main_df = sns.load_dataset('planets')
# print(main_df.head())

penguins = sns.load_dataset('penguins')
# print(penguins.columns)
# 'species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex'],
penguins.groupby(['species'])['body_mass_g'].mean()

# print(penguins.groupby(['sex']).body_mass_g.sum())

# print(penguins.groupby(['sex', 'island']).bill_depth_mm.max())



# print(penguins.groupby(['species', 'sex']).body_mass_g.max().reset_index(name='Max. Mass'))

penguins['Bill 2 Flipper ratio'] = penguins.bill_length_mm / penguins.flipper_length_mm;
print(penguins.groupby(['species', 'sex'])['Bill 2 Flipper ratio'].mean().reset_index(name='Ø F2BR'))
#.reset_index(name='Bill 2 Flipper ratio'))