import numpy as np
import pandas as pd

# series_new = pd.Series(np.random.randint(0, 500, 1500))

# for item in series_new:
#     print(type(item))
#     exit()
words = ["Sven", "is", "hunting", "Doc Ock", "and", "Venom"]
my_series = pd.Series(
    words, index=range(1, len(words) + 1), name="The name of the Series"
)

print(my_series)


## todo
### - Broadcasting
