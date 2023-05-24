import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import os
import csv

with open('../data.csv', encoding='utf-8')as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'wafer id':
            header = row
            csv_dict = {i:[] for i in header}
        else:
            if row.count('') > 10:
                continue
            for i,j in enumerate(header):
                try:
                    row[i] = np.float64(row[i])
                except:
                    pass
                finally:
                    csv_dict[j].append(row[i])

data = pd.DataFrame(csv_dict)
#data = data.T
data.set_index(['wafer id', 'angle'], inplace=True, drop=True)

r_cols = header[2:]
print(r_cols)

r_locs = np.float64(r_cols)





