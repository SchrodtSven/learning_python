import pandas as pd
import numpy as np

colored_key_series = pd.Series({"Rot": 13, "Blau": 24, "Grün": 1, "Schwarz": 90, "Magenta": 3})
#print(colored_key_series)

# colored_key_series["Schwarz"]
#print(colored_key_series.index[-2])

print(colored_key_series["Schwarz"])

print(colored_key_series.values[-2])



print(colored_key_series.values)
print(colored_key_series.index)


# Get a list of random numbers 



# my_rnd_nums = pd.Series(np.random.randrange(1,1001) for x in range(5))
# print(my_rnd_nums)

print(np.random.randint(1,100, 66))