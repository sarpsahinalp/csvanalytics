import pandas as pd

df = pd.read_csv('natives.csv')

# get me all the columns where kind column is equal to 'files'
print(df[df['kind'] == 'files'])

# save it another csv file
df[df['kind'] == 'files'].to_csv('files.csv', index=False)
