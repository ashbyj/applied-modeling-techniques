import pandas as pd 
import sklearn
from os.path import dirname
from sys import argv

df = pd.read_csv((dirname(argv[0]) + '/diamonds.csv'))
print(df)

df = df.drop(df.columns[[0]], axis=1)

print(df)
