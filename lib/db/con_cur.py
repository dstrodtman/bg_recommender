import psycopg2 as pg2
from psycopg2.extras import RealDictCursor

def bgg_tuples():
    con = pg2.connect(host='35.165.233.229',
                  dbname='postgres',
                  user='postgres')
    cur = con.cursor()
    return con, cur

def bgg_dict():
    con = pg2.connect(host='35.165.233.229',
                  dbname='postgres',
                  user='postgres')
    cur = con.cursor(cursor_factory=RealDictCursor)
    return con, cur