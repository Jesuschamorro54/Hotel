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
            sql = f"select id, user_id, room_id, descriptions, likes, state, fecha from {table} WHERE state = 1"
    # comments generales-----
        elif table == "general_comments":
            sql = f"select user_id, nombre,room_id, descriptions, likes, state, fecha from {table} WHERE state = 1"
    # reservas -----
        elif table == "reservas":

            # Este es el mio
            sql = f"""SELECT r.id, u.nombre, r.solicitado, r.date_inicio, r.date_final, r.state  FROM reservas r
                        INNER JOIN users u on u.id = r.user_id
                        WHERE r.state in (0, 1);"""

    # rooms -----
        elif table == "rooms":
            sql = f"select id, numero, descriptions, calification, image, price, enabled from {table} WHERE state = 1 and enabled = 1"
    # payments -----
        elif table == "payments":
            sql = f"select id, nombre, email, rol, image from {table} WHERE state = 1"

        if sql != '':
            cursor.execute(sql)
            container = cursor.fetchall()
            #print(f"\n|R-DB - {table}|:")
            #for item in container:
            #    print(item)
        else:
            print("---|SQL NULL|---")
            container = ""

    return container


# BUSCAR UN REGISTRO
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
            print(f"|R-DB - {table}| ")
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
            sql = f"UPDATE {table} SET state = -1 WHERE (id = {id});"

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


def update(data):
    sql = ''
    conexion, cursor = DataBase.connect(d)
    with cursor:
    
        # users -----
        if data['table'] == 'users':
            sql = f"""UPDATE users SET 
            nombre = "{data['nombre']}", 
            email = "{data['email']}", 
            rol = "{data['rol']}"
            WHERE (id = {int(data['id'])})"""

        # ROOMS -----
        elif data['table'] == 'rooms':
            sql = f"""UPDATE rooms SET 
            numero = "{data['number']}", 
            price = {data['price']}, 
            descriptions = "{data['descriptions']}"

            WHERE (id = {int(data['id'])})"""

        # RESERVAS -----
        elif data['table'] == 'reservas':
            sql = f"""UPDATE reservas SET 
            state = {data['state']}
            WHERE (id = {int(data['id'])})"""

        # EJECUCIÓN DE SQL
        try:
            cursor.execute(sql)
            print("\nR-DB: EDICION COMPLETADA!")
            conexion.commit()
            conexion.close()
        except Exception as e:
            print("\nR-DB: ERROR EN LA EDICIÓN!\n")
            print(e)


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

# INSERTAR DATOS DE UNA TABLA
def addreg(table,parameters):
    print(parameters)
    sql = ""
    conexion, cursor = DataBase.connect(d)
    with cursor:
        conexion.begin()

    # users -----
        if table == "users":
            sql = f"""INSERT INTO {table}(nombre, email, password, image, fuente, rol, city, state) 
        VALUES ('{parameters}')"""
    # comments -----
        elif table == "comments":
            sql = f"""INSERT INTO {table}(user_id, room_id, descriptions, likes, state, fecha) 
        VALUES ('{parameters}')"""
    # reservas -----
        elif table == "reservas":
            sql = f"""INSERT INTO {table}(user_id, room_id, descriptions ,solicitado, date_inicio, date_final, state, q_adults, q_childrens, q_days)
            VALUES(
                {parameters['user_id']}, {parameters['room_id']}, '{parameters['descriptions']}', 
                '{parameters['solicitado']}', '{parameters['date_inicio']}', '{parameters['date_final']}', 
                {parameters['state']}, {parameters['q_adults']}, {parameters['q_childrens']}, {parameters['q_days']}
            )"""
    # rooms -----
        elif table == "rooms":
             sql = f"""INSERT INTO {table}(numero, descriptions, calification, image, price, enabled) 
        VALUES ('{parameters}')"""
    # payments -----
        elif table == "payments":
            sql = f"""INSERT INTO {table}(nombre, email, rol, image) 
        VALUES ('{parameters}')"""

        if sql != '':
            try:
                cursor.execute(sql)
                print("\nR-DB: INSERCIÓN COMPLETADA!")
                conexion.commit()
                conexion.close()
            except Exception as e:
                print("\nR-DB: ERROR EN LA INSERCIÓN!\n")
                print(e)
        else:
            print("---|SQL NULL|---")


#def insertar_reservas(user_id, room_id, descriptions ,solicitado, date_inicio, date_final, state, q_adults, q_childrens, q_days):
#
#    # Ahora Database devuelve dos valores
#    # *conexion* gestiona la base de datos, mientras que cursor se encarga de las consultas e inserciones
#    conexion, cursor = DataBase.connect(d)
#    with cursor:
#        sql = f"""INSERT INTO reservas(user_id, room_id, descriptions ,solicitado, date_inicio, date_final, state, q_adults, q_childrens, q_days) 
#        VALUES ('{user_id}','{room_id}','{descriptions}','{solicitado}','{date_inicio}','{date_final}','{state}','{q_adults}','{q_childrens}','{q_days}')"""
#
#        # Enviar un mensaje si la inserción fue exitosa
#        print("Inserción exitosa!") if cursor.execute(sql) else ("Error en la inserción")
#                    
#    conexion.commit()
#    conexion.close()