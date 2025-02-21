import seaborn as sns

taxis = sns.load_dataset('taxis')

print(type(taxis))

# print(taxis[taxis['color']=='green', taxis['pickup_borough'] == 'Queens'] )