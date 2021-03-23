#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pubchempy as pcp
import pandas as pd
from collections import deque
import sys
data = pd.read_csv("compounds.csv", header=None)
list_of_compounds = list(data[0])
for i in list_of_compounds:
    try:
        pcp.download('SDF', f'{i}.sdf', i, 'name', record_type = '3d')
    except:
        with open('not_downloaded.txt', 'a') as f:
            print(i, file=f)
