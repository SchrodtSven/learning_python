import seaborn as sns

# print(sns.get_dataset_names())
# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 
# 'diamonds', 'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 
# 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 
# 'taxis', 'tips', 'titanic']


dataset = sns.load_dataset('exercise')
print(dataset.head())
# print(dataset['origin'].unique())
