import psycopg2
import psycopg2.extras

sql =  'SELECT "WAFER_ID"\
        FROM phm_data.training_set_x\
        WHERE "STAGE"=\'B\';'

conn_string = "host='localhost' dbname='phm2016' user='postgres' password='WeiDian0930'"
conn = psycopg2.connect(conn_string)

if conn is not None:
    print('Connection established to PostgreSQL.')

cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
cursor.execute(sql)
records = cursor.fetchone()
print(records)

# for row in records:
#     print(row)

cursor.close()
conn.close()

# engine = create_engine('postgresql://postgres:WeiDian0930@localhost:5432/phm2016')

# wafers = pd.read_sql(sql, con=engine)
# print(wafers.shape)
