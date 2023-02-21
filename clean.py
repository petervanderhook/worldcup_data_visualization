import pandas as pd

#   Load the original CSV File
df = pd.read_csv('worldcup.csv')

#   Remove the rows where types = 'Caps'
df = df[df['Type'] != 'Caps']

#   Now that duplicate rows are removed, remove the entire type column
df = df.drop(columns=["Type"])

#   Name the first column of index numbers.
df.index.name = 'id'

#   Save the dataframe to a csv file
df.to_csv('worldcup_clean.csv')