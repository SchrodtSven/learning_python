import pandas as pd


temp = [4.5, 6.3, 3.8, 5.1, 4.9, 5.7, 4.2, 6.0]
times = [
    '2023-01-01 19:08',
    '2023-01-01 18:17',
    '2023-01-01 06:03',
    '2023-01-01 02:17',
    '2023-01-01 22:02',
    '2023-01-01 16:00',
    '2023-01-01 21:04',
    '2023-01-01 11:16'
]
barometric_pressure = {
    'Location': [
        'Berlin', 'München', 'Wilhelmshaven',
        'Kassel', 'Frankfurt', 'Duisburg',
        'Dresden', 'Würzburg'
    ],
    'Press': [
        1001.2, 997.8, 1002.5, 1000.1,
        998.9, 1001.5, 999.2, 1002.8
    ],
    'Temp': temp,
    'Times': times
}
geo_dict = {
    'Location': [
        'Berlin', 'München', 'Hamburg', 'Köln',
        'Frankfurt', 'Duisburg', 'Kassel', 'Würzburg'
    ],
    'Lat': [52.31, 48.8, 53.33, 45.75, 47.61, 53.55, 49.28, 51.05],
    'Long': [13.24, 11.34, 10.0, -122.43, -122.33, -113.49, -123.13, -114.07]
}
location_order = [
    "Berlin", "Frankfurt", "München", "Kassel",
    "Duisburg", "Dresden", "Würzburg", "Wilhelmshaven",
    "Hamburg", "Köln"
]
desired_cols = ["Press", "Lat", "Long", "Temperature", "Timestamp"]


foo = pd.DataFrame(geo_dict).merge(pd.DataFrame(barometric_pressure), on='Location', how='outer')
foo.set_index('Location', inplace=True)
foo.reindex(location_order).sort_values('Location')
print(foo)

# 52.31, 13.24