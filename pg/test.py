import pandas as pd
import psycopg2

connection = psycopg2.connect(
host='localhost',
port='5433',
user='postgres',
password='PG_root23@',
database='northwind'
)

#df = pd.read_sql_query("SELECT * FROM products", con=connection)

df = pd.read_sql("SELECT * FROM region", con=connection)
print(df)