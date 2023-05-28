import os.path
import pandas as pd
from sqlalchemy import create_engine

folder = r'C:\Users\diany\OneDrive\文档\Github\phm2016\data'
name = 'training_set_y.csv'

file = os.path.join(folder, name)

engine = create_engine('postgresql://postgres:WeiDian0930@localhost:5432/phm2016')

df = pd.read_csv(file, header=0)

df.to_sql('training_set_y', engine, index=False, schema='phm_data', if_exists='append')

