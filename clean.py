import matplotlib as plt 
import numpy as np
import pandas as pd


df = pd.read_csv('worldcup.csv')

#clean the dataframe remove the rows with types= 'Caps'
df = df[df['Type'] != 'Caps']

#remove the entire type column
df = df.drop('Type', axis=1)


#save the dataframe to a csv file
df.to_csv('worldcup_clean.csv')


df2 = pd.read_csv('worldcup_clean.csv')
df2.index.name = 'id'

#plot the dataframe using matplotlib
plty = df2.plot(kind='scatter',  x='Goals', y='Caps', title='World Cup Goals to Caps Scatter Plot')

plty.set_xlabel('Goals')
plty.set_ylabel('Caps')
plty.show()