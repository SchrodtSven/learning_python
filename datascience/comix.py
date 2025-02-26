import pandas as pd

characters = pd.read_csv('archive/marchar.csv')

# print(characters.name.head(34))

print(characters.columns)


def get_x_split_by(x):
    tmp = x.split()
    if(len(tmp)<2):
        return None
    return tmp[0]

characters['name_civil'] = characters.name.map(lambda  x: x[x.find('(') +1 : x.find(')')])

characters['char_name']  = characters.name.map(lambda  x: x[0: x.find('(')])



#= characters['name'].map(get_x_split_by)

sliced = characters[['name_civil', 'char_name', 'FIRST APPEARANCE', 'Year', 'ID']]
print(sliced.head())
