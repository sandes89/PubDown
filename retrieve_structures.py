import os
import pubchempy as pcp
import pandas as pd
from collections import deque

list_compounds = pd.read_csv("compounds.csv", header=None)

data = list(list_compounds[0])
len(data)

Compounds = {}
for i in data:
        a = pcp.get_compounds(i, 'name')
        Compounds[i] = a
len(Compounds)

no_result = [] 
for i in (Compounds):
    if (Compounds[i] == []):
        no_result.append(i)
    
len(no_result)

for i in deque(Compounds.keys()):  #Deque helps to remove elements from any part of the dictionary; remove the no_result IDs from original dictionary
    for j in no_result:
        if i == j:
            del Compounds[i]

len(Compounds)

for i in Compounds:
    try:
        pcp.download('SDF', f'{i}.sdf', i, 'name', record_type = '3d' )
    except:
        print(i)


no_result
