#!/usr/bin/env python3
# datascience/dsj
#
# SUBJECT: Playground for Pandas' DataFrame with data science jobs salary etc.
# AUTHOR: Sven Schrodt <sven@schrodt.club>
# SINCE: 2025-02-26
import numpy as np
import pandas as pd

jobs = pd.read_csv('data_jobs.csv')
# print(jobs.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 127 entries, 0 to 126
# Data columns (total 13 columns):
 #   Column              Non-Null Count  Dtype 
# ---  ------              --------------  ----- 
#  0   Unnamed: 0          127 non-null    int64 
#  1   job_title           127 non-null    object
#  2   experience_level    127 non-null    object
#  3   employment_type     127 non-null    object
#  4   work_models         127 non-null    object
#  5   work_year           127 non-null    int64 
#  6   employee_residence  127 non-null    object
#  7   salary              127 non-null    int64 
#  8   salary_currency     127 non-null    object
#  9   salary_in_usd       127 non-null    int64 
#  10  company_location    127 non-null    object
#  11  company_size        127 non-null    object
#  12  salary_level        126 non-null    object
# dtypes: int64(4), object(9)
# memory usage: 13.0+ KB

max = jobs.groupby(['company_location'])['salary_in_usd'].max()
col_max = jobs.groupby(['company_location'])['salary_in_usd'].idxmax()


# print(max, col_max)

# print(jobs.get(123))


# idx = jobs.index == 123
# print(jobs.tail(12))

# print(jobs.loc[123])

# bool_mask = jobs['salary_in_usd'] > 80000
# print(bool_mask)
# print(jobs[bool_mask])


print(jobs['work_year'].value_counts())
# jobs.info()

result = jobs['salary'].agg(['max', 'mean', 'min', 'std'])
print(result)
# result.agg(lambda x : np.mean(x))
# np.number

