import pandas as pd
import numpy as np
from palmerpenguins import load_penguins

penguins = load_penguins()
print(penguins.shape)
print(penguins.columns)
print('-'*30)

penguins.dropna(inplace=True)
print(penguins.isna().any())
print('-'*30)

print(penguins.groupby(['sex'])['sex'].count())
print('-'*30)
print(penguins.groupby(['sex']).aggregate({
     'bill_length_mm':np.mean}))
print('-'*30)

penguins['bill_area'] = penguins['bill_length_mm'] * penguins['flipper_length_mm']
print(penguins.columns[-1])
print('-'*30)
bySpeciesSex=penguins[penguins.sex=='female'].groupby(['sex','species'])
print(bySpeciesSex.describe())
print('-'*30)

penguins['body_mass_kg'] = penguins['body_mass_g']/1000
penguins.drop(columns=['body_mass_g'],inplace=True)
print(penguins.head())