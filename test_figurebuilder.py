import pandas as pd
import matplotlib as plt

df = pd.read_json('cars.json')
fig, ax = plt.subplots()
df['Car Name'].value_counts().plot(ax=ax, kind='bar') # gets frequency of car name and plots it into a bar graph

df.head() # shows top few rows in dataframe

"""Convert columns to numeric and date as follows"""
df['price_int'] = df['Price'].str.replace(r'\xa0K\t\t', '') # this removes extraneous information from pulled numbers, r is used to ignore \ as escape sequences
df['price_int'] = df['Price'].str.replace(r'\xa0K\t\t', '').convert_objects(convert_numeric=True) # converts string to numpy.float. This however has been deprecated
pd.to_numeric(df['price_int']) # does the same as above, but for some reason breaks with commas, maybe stick with above.
df.to_csv('{{filename}}') # saves dataframe to useful csv form, this makes life so much easier omg

