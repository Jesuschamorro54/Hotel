
# Hotel
Este proyecto, desarrollado para MinTic, tiene como objetivo crear una aplicación web con la capacidad de ofrecer diferentes opciones a los usuarios para elegir la mejor habitación para su alojamiento en un hotel.

#### Contenido 
* [Base de datos](#base-de-datos)
* [Run](#run)

### BASE DE DATOS
Se implementa el manejador de bases de datos [Mysql](https://www.mysql.com), el cual puede realizar la descarga desde la pagina oficial que se encuenta en el link. O también puede intentar descargar con:
* [Windows (x86, 32-bit), MSI Installer](https://dev.mysql.com/downloads/file/?id=506568)

    ***Nota:*** *No es necesario realizar un **login** o **sing up**, solo debe dar clic en la opción "No thanks, just start my download" que se encuentra en la parte inferior.*

* ### Tutorial para instalar Mysql Server y Workbench
    [Instalación - Tutorial](https://www.youtube.com/watch?v=Sv2vBT3dtvQ)

*   ### Creacion de la base de datos
    Una vez instalado todos los recursos a utilizar, puede ejecutar los comandos de DDL encontrados en la ruta:

    `hotel/app/Files/database_creation.sql`

### RUN
Para correr la aplicación, instale en su equipo el framework `flask` con el cual podrá correr en su ip personal la página web. Para ello debe ejecutar en su `cmd`:

#### Install
```
C:\Users> pip install flask
```

***Nota:*** *Es esencial que tenga instalado el gestor de paquetes `pip` con el cual se realizará la instalación. [Install](https://pip.pypa.io/en/stable/installation/#)*

* #### Activate
    Ir a la carpeta raiz del repositorio `/hotel` en la terminal de     comandos, dirigirse a la ruta `hotel\app\Scripts` y ejecutar:

    ```
    activate
    ```
* #### Run
    Luego en la ruta `hotel\app`
    ```
    flask run
    ```
