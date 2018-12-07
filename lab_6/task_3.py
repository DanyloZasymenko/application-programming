import matplotlib.pyplot as plot
import pandas as pd

df = pd.read_csv('NYC_Jobs.csv')
names = ['Agency', '# Of Positions']
print(df[names])
df['Agency'].value_counts(sort=True).plot.bar()
plot.show()
