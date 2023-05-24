from sqlalchemy import create_engine

# 方法一， 利用sqlalchemy_utils库的create_databse模块
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('mysql+pymysql://root:WeiDian0930@localhost:3306/spyderdb')
if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))


