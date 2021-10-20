import pymysql
from pymysql import Error
from flask import current_app, g

def get_db():

    try:
        if 'db' not in g:
            class DataBase:
                def __init__(self, name_database):
                    self.name = name_database
                    self.connection = pymysql.connect(host='localhost', user='root', password='', db=f'{self.name}')

            g.db = DataBase('hoteles.db')
            print('conectada')
            return g.db
    except Error:
        print(Error)


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()