import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:WeiDian0930@localhost:5432/phm2016')

sql = 'SELECT * FROM phm_data.training_set_x WHERE "STAGE"=\'B\' AND "MACHINE_DATA"=4'

df = pd.read_sql(sql, con=engine)
print(df)
