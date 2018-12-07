import pandas as pd

df = pd.read_csv('NYC_Jobs.csv')
print(df['Agency'][:10])

print('------------------------------------------------------')

data = pd.read_csv('NYC_Jobs.csv')
pd.options.display.max_columns = 3
print(data[['Agency', 'Business Title', 'Work Location 1']].to_string(index=False))
