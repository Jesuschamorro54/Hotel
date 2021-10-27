from pymysql import NULL
from werkzeug.wrappers import response
from db import DataBase

# Variable glogal que contiene la informacion de la base de datos
d = {
        "host": "localhost",
        "user": "root",
        "password": "20023006",
        "db": "hotel"
}

def insertar_user(nombre, email, password):

    # Ahora Database devuelve dos valores
    # *conexion* gestiona la base de datos, mientras que cursor se encarga de las consultas e inserciones
    conexion, cursor = DataBase.connect(d)
    with cursor:
        sql = f"""INSERT INTO users(nombre, email, password, image, fuente, rol, city, state) 
        VALUES ('{nombre}','{email}', '{password}', null, 'google', 'free', 'Barranquilla', 1)"""

        # Enviar un mensaje si la inserción fue exitosa
        print("Inserción exitosa!") if cursor.execute(sql) else ("Error en la inserción")
                  
    conexion.commit()
    conexion.close()


# TRAER TODOS LOS DATOS DE UNA TABLA
def consultar(table):
    sql = ""
    conexion, cursor = DataBase.connect(d)
    with cursor:
        conexion.begin()
# users -----
        if table == "users":
            sql = f"select id, nombre, email, rol, image from {table} WHERE state = 1"
# comments -----
        elif table == "comments":
            sql = f"select id, nombre, email, rol, image from {table} WHERE state = 1"
# reservas -----
        elif table == "reservas":
            sql = f"select id, nombre, email, rol, image from {table} WHERE state = 1"
# rooms -----
        elif table == "rooms":
            sql = f"select id, numero, descriptions, calification, image, price, enabled from {table}"
# payments -----
        elif table == "payments":
            sql = f"select id, nombre, email, rol, image from {table} WHERE state = 1"

        if sql != '':
            cursor.execute(sql)
            container = cursor.fetchall()
            print(f"|R-DB - {table}|: ", container)
        else:
            print("---|SQL NULL|---")
            container = ""

    return container


# BUSCAR UN REGISTRO UN REGISTRO
def find(parameter, tp, table):

    """
    parameter: Es el parametro por el que se va a buscar, ya sea id, nombre, description, fecha o email, etc.
    #--------------------------------------------------------------------------------------------------------
    tp: Es el tipo de ese parametro, recibe str o number
    #--------------------------------------------------------------------------------------------------------
    table: Es la tabla que se va a consultar
    """

    conexion, cursor = DataBase.connect(d)
    conexion.begin()
    sql = ""
    with cursor:
    # users -----
        if table == 'users':
            if tp == 'number':
                sql = f"select id, nombre, email, rol, image from users WHERE id = {parameter} and state = 1"
            elif tp == 'str':
                sql = f"select id, nombre, email, rol, image from users WHERE (nombre like '%{parameter}%' or email = '{parameter}') and state = 1"
    # rooms -----   
        elif table == 'rooms':
            if tp == 'number':
                sql = f"select id, numero, descriptions, calification, image, price, enabled from {table} WHERE id = {parameter}"
            elif tp == 'str':
                sql = f"select id, numero, descriptions, calification, image, price, enabled from {table} WHERE numero = {parameter}"
    # comments -----
        elif table == 'comments':
            pass # CODIGO DE ESTE CONDICIONAL

    # reservas -----
        elif table == 'reservas':
            pass # CODIGO DE ESTE CONDICIONAL

    # payments -----
        elif table == 'payments':
            pass # CODIGO DE ESTE CONDICIONAL

    #---------------------Ejecutar el sql-------------------------
        if sql != '':
            cursor.execute(sql)
            container = cursor.fetchone()
            print(f"|R-DB - {table}|: ", container)
        else:
            print("---|SQL NULL|---") # Muestra esto por consola si el sql queda nulo
            container = ""

    return container  # Retorna los datos que se buscan


# ELIMINAR UN REGISTRO
def eliminar(id, table):
    print("Eliminando usuario")
    conexion, cursor = DataBase.connect(d)
    with cursor:
    
    # users -----
        if table == 'users':
            sql = f"UPDATE {table} SET state = -1 WHERE (id = {id});"

    # rooms -----
        elif table == 'rooms':
            pass # CODIGO DE ESTE CONDICIONAL

    # comments -----
        elif table == 'comments':
            pass # CODIGO DE ESTE CONDICIONAL

    # reservas -----
        elif table == 'reservas':
            pass # CODIGO DE ESTE CONDICIONAL

    # payments -----
        elif table == 'payments':
            pass # CODIGO DE ESTE CONDICIONAL

        # Enviar un mensaje si la inserción fue exitosa
        print(f"Eliminación exitosa!: user_id: {id}") if cursor.execute(sql) else ("Error en la Eliminación")
                  
    conexion.commit()
    conexion.close()


# OBTENER UN USUARIO POR EMAIL
def obtener_user(usr_email):
    conexion, cursor = DataBase.connect(d)
    info_user = None
    with cursor:
        sql = f"SELECT id, nombre, email, password, rol FROM users WHERE email = '{usr_email}'"
        cursor.execute(sql)
        info_user = cursor.fetchone()
    conexion.close()
    return info_user

