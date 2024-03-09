# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:52:59 2024

@author: mayil
"""

import numpy as np
import pandas as pd

"""
From df filter the 'Manufacturer', 'Model' 
and 'Type' for every 20th row starting 
from 1st (row 0).
"""
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df1 = df.loc[:,"Manufacturer":"Type"]

print(df1.head())

print("-----------------------")
#Replace missing values in Min.Price and Max.Price columns 
#with their respective mean.
# Calculate the mean for 'Min.Price' and 'Max.Price'
min_price_mean = df['Min.Price'].mean()
max_price_mean = df['Max.Price'].mean()

# Replace missing values with their respective means
df['Min.Price'].fillna(min_price_mean, inplace=True)
df['Max.Price'].fillna(max_price_mean, inplace=True)

# Display the DataFrame after filling missing values
print(df.head())

print("-----------------------")


df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
row_sums = df.sum(axis=1)

# Filter rows with sum > 100
rows_greater_than_100 = df[row_sums > 100]

# Display the result
print("Rows with Row Sum > 100:")
print(rows_greater_than_100)
