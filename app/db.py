import pymysql
from flask import g

class DataBase:
    # DB es un diccionario que contine los datos para crear la conexion
    def connect(db):
        """
        Conectarse a travéz de un diccionario tiene la ventaja de que cuando necesita conectar
        multiples bibliotecas y tablas, puede crear múltiples diccionarios para distinguirlos.
        :return : Devuelve la conexion si la base de datos existe y el cursor de la base de datos mysql       
        """
        try:
            connection = pymysql.connect(host=db["host"], user=db["user"], passwd=db["password"], db=db["db"])
            cursor = connection.cursor() # se crea el cursor de datos mysql 
            print("Connection established")
        except Exception as e:
            connection = pymysql.connect(host=db["host"], user=db["user"], passwd=db["password"], db=db["db"])
            cursor = connection.cursor() # se crea el cursor de datos mysql 
            print("Error connecting to database", e)
        return cursor

d = {
    "host": "localhost",
    "user": "root",
    "password": "Xricagomex0126.",
    "db": "hotel"
}
Dbase = DataBase.connect(d)