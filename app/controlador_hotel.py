from db import DataBase

def insertar_user(nombre, email, password):
    conexion = DataBase.connect()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO juegos(nombre, email, password, image, fuente, rol, city, state) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (nombre, email, password, '', 'google', 'free', 'Barranquilla', "Atlantico"))
    conexion.commit()
    conexion.close()