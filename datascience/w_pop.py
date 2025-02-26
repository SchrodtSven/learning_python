import pandas as pd

def sanitize_number(number: str):
    return int(number.replace(',', ''))
pop = pd.read_csv('populaton_world.csv')

print(pop.head)

pop['pop_int'] = pop['Population (2024)'].map(sanitize_number)
print(pop.head())

print(pop['pop_int'].sum())