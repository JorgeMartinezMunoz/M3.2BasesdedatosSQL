import mysql.connector
from mysql.connector import Error


def conectar_a_mysql():
    try:
        # Paso 3: Establecer la conexión
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto a la dirección de tu servidor MySQL
            database='u927419088_testing_sql',  # Cambia esto por el nombre de tu base de datos
            user='u927419088_admin',  # Cambia esto por tu usuario de MySQL
            password='#Admin12345#'  # Cambia esto por tu contraseña de MySQL
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")

            # Paso 4: Crear un cursor para realizar operaciones en la base de datos
            cursor = connection.cursor()

            # Paso 5: Ejecutar una consulta
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Conectado a la base de datos: {record}")

            # Ejemplo: Obtener todas las tablas de la base de datos
            cursor.execute("SHOW TABLES;")
            tablas = cursor.fetchall()
            print("Tablas en la base de datos:")
            for tabla in tablas:
                print(tabla)

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        # Paso 6: Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


# Llamar a la función para conectarse a MySQL
conectar_a_mysql()