import pandas as pd

cities = {
    "name": [
        "London",
        "Berlin",
        "Madrid",
        "Rome",
        "Paris",
        "Vienna",
        "Bucharest",
        "Hamburg",
        "Budapest",
        "Warsaw",
        "Barcelona",
        "Munich",
        "Milan",
    ],
    "population": [
        8615246,
        3562166,
        3165235,
        2874038,
        2273305,
        1805681,
        1803425,
        1760433,
        1754000,
        1740119,
        1602386,
        1493900,
        1350680,
    ],
    "country": [
        "England",
        "Germany",
        "Spain",
        "Italy",
        "France",
        "Austria",
        "Romania",
        "Germany",
        "Hungary",
        "Poland",
        "Spain",
        "Germany",
        "Italy",
    ],
}

cty = pd.DataFrame(cities)
# print(cty)

city_reindexed = pd.DataFrame(cities,
columns = ['name', 'population'],
index = cities['country'])


print(city_reindexed)