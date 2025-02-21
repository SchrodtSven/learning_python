import seaborn as sns

curr_ds = sns.load_dataset('penguins')
foo = curr_ds.loc[[100,234], ['body_mass_g']]

print(curr_ds.head())

print(curr_ds['island'].unique())
# .select_dtypes('object') --> TypeError("string dtypes are not allowed, use 'object' instead")
print(curr_ds.select_dtypes('object').describe())

