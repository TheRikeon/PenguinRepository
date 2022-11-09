import pandas as pd
import numpy as np
from palmerpenguins import load_penguins

penguins = load_penguins()
print(penguins.shape[0]) #miramos la primera posición de shape para ver el número de observaciones
print('-'*30,end='\n \n') #separador del output para tener mayor claredad, el \n \n incluye una línea vacía extra respecto al valor por defecto también por claredad
print(penguins.columns) #miramos los nombres de las columnas
print('-'*30,end='\n \n')
print(penguins.info()) #miramos las caracteristicas del df y el tipo de datos de cada columna
print('-'*30,end='\n \n')

penguins.dropna(inplace=True) #quita todas las filas que tengan algún NA y utilizamos inplace=True para evitar crear variables nuevas
print(penguins.isna().any()) #comprobamos que ninguna columna tenga valores NA
print('-'*30,end='\n \n')

print(penguins.groupby(['sex'])['sex'].count()) #agrupamos segun el genero y contamos segun el genero para ver su cantidad
print('-'*30,end='\n \n')
print(penguins.groupby(['sex']).aggregate({ 
     'bill_length_mm':np.mean})) #agrupamos segun el sexo y calculamos la media de bill_length_mm de cada grupo
print('-'*30,end='\n \n')

penguins['bill_area'] = penguins['bill_length_mm'] * penguins['bill_depth_mm'] #creamos una nueva columna llamada bill_area que es el resultado de multiplicar cada elemento de bill_length_mm por su correspondiente de bill_depth_mm
print(penguins.columns[-1]) #miramos las columnas del df y miramos la ultima posicion para comprobar que es bill_area
print('-'*30,end='\n \n')

bySpeciesSex=penguins[penguins.sex=='female'].groupby(['sex','species']) #filtramos el sexo femenino y luego agrupamos por sexo y especie
print(bySpeciesSex.describe()) #visualizamos información de las hembras segun la especie
print('-'*30,end='\n \n')

penguins['body_mass_kg'] = penguins['body_mass_g']/1000 #creamos una nueva columna llamada body_mass_kg que sea la columna de peso en gramos partido 1000 para pasarlo a kg
penguins.drop(columns=['body_mass_g'],inplace=True) #eliminamos la columna body_mass_g con inplace=True para evitar variables nuevas
print(penguins.head()) #comprobamos la nueva columna