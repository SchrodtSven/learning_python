import numpy as np
import pandas as pd

my_dict = {
            'name': ['Gil', 'Lana', 'Noel', 'Cliff'],
            'age':[72, 45, 70, 83]
    
}

df = pd.DataFrame(my_dict)
ndf = pd.concat([df,pd.DataFrame({'name': ['Sahra'], 'age': [33]})], ignore_index=True)
#print(ndf['age'])

# index location [line, col(s)] in known "idx|slc Syntax"
#print(ndf.iloc[:,1]) # all lines; 2. column only


# print(ndf)
# exit()

# filtering index labels::
foo = ndf.loc[ndf['age']>58]



# Changing values !! 
# foo = ndf.loc[ndf['age']>71, 'name']!='Gil'

print(foo)