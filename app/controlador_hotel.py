from db import DataBase

# Variable glogal que contiene la informacion de la base de datos
d = {
        "host": "localhost",
        "user": "root",
        "password": "Xricagomex0126.",
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


#insertar_user("enrique", "enrique@gmail.com", "hola123") # -> Inserción de prueba

def obtener_user(email):
    conexion, cursor = DataBase.connect(d)
    info_user = None
    with cursor:
        cursor.execute(
            "SELECT id, nombre, email, password, rol FROM users WHERE email = %s", (email,))
        info_user = cursor.fetchone()
    conexion.close()
    return info_user