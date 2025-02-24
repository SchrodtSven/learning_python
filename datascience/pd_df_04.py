#!/usr/bin/env python3
# datascience/pd_df_04.py
# 
# SUBJECT: Playground for Pandas' DataFrame
# AUTHOR Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-01-03

import pandas as pd

my_index = ["Alice", "Bob", "Claudette", "Danielle", "Émile"]
df1 = pd.DataFrame(
    {
        "Age": [25, 30, 22, 27, 18],
        "Location": ["Berlin", "München", "Hamburg", "Köln", "Concarneau"],
    },
    index = my_index,
)

df2 = pd.DataFrame(
    {
        "Ranking": [60, 75, 55, 80, 99.1], 
        "Length": [170, 180, 165, 185, 199]
    },
    index = my_index,
)

# df2.columns = df2.index
foo = pd.concat([df1, df2], axis = 1)
# clarification: one may choose to specify axis='index' (instead of axis=0) or axis='columns' (instead of axis=1)
# Usually axis=0 is said to be "column-wise" (and axis=1 "row-wise")
# A        B
# 0  0.626386  1.52325  → → axis=1 → →
#           ↓        ↓
#           ↓ axis=0 ↓
#           ↓        ↓


print(foo)
