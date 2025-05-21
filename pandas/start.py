import pandas as pd

print(pd.options.display.max_rows) 
# 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

# You can change the maximum rows number with the same statement.
pd.options.display.max_rows = 9999

