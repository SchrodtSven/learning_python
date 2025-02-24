import pandas as pd

# Temperatur-Messwerte
temp = [4.5, 6.3, 3.8, 5.1, 4.9, 5.7, 4.2, 6.0]

# Zeitstempel für Messzeitpunkt
times = [
    "2023-01-01 19:08",
    "2023-01-01 18:17",
    "2023-01-01 06:03",
    "2023-01-01 02:17",
    "2023-01-01 22:02",
    "2023-01-01 16:00",
    "2023-01-01 21:04",
    "2023-01-01 11:16",
]

# Orte und Luftdruckmessung
meteo_dict = {
    "Location": [
        "Berlin",
        "München",
        "Wilhelmshaven",
        "Kassel",
        "Frankfurt",
        "Duisburg",
        "Dresden",
        "Würzburg",
    ],
    "Barometric_Pressure": [1001.2, 997.8, 1002.5, 1000.1, 998.9, 1001.5, 999.2, 1002.8],
}

df_temp_time = pd.DataFrame({"ts": times, "temp": temp})
print(df_temp_time)
df_meteo = pd.DataFrame(meteo_dict)
# print(meteo_dict)
# lonf / lat
geo_dict = {
    "Location": [
        "Berlin",
        "München",
        "Hamburg",
        "Köln",
        "Frankfurt",
        "Duisburg",
        "Kassel",
        "Würzburg"
    ],
    "Latitude": [52.31, 48.8, 53.33, 45.75, 47.61, 53.55, 49.28, 51.05],
    "Longitude": [13.24, 11.34, 10.0, -122.43, -122.33, -113.49, -123.13, -114.07],
}

df_geo = pd.DataFrame(geo_dict)
df_new = df_meteo.merge(df_geo, on="Location")

print(df_new)
