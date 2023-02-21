import matplotlib as plt 
import numpy as np
import pandas as pd


df = pd.read_csv('worldcup.csv')

#clean the dataframe remove the rows with types= 'Caps'
df = df[df['Type'] != 'Caps']

#remove the entire type column
df = df.drop(columns=["Type"])
df.index.name = 'id'

#save the dataframe to a csv file
df.to_csv('worldcup_clean.csv')