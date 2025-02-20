import numpy as np
import pandas as pd

series_new = pd.Series(np.random.randint(0, 500, 1500))

for item in series_new: 
    print(type(item))
    exit()

