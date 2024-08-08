import mysql.connector
import pandas as pd
from mysql.connector import Error

def obtener_registros_avanzados():
    try:
        # Establecer la conexión a la base de datos
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto a la dirección de tu servidor MySQL
            database='u927419088_testing_sql',  # Cambia esto por el nombre de tu base de datos
            user='u927419088_admin',  # Cambia esto por tu usuario de MySQL
            password='#Admin12345#'  # Cambia esto por tu contraseña de MySQL
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")

            # Crear un cursor para realizar operaciones en la base de datos
            cursor = connection.cursor()

            # Consultar los registros donde el nivel es 'Avanzado'
            query = "SELECT * FROM profesor;"
            cursor.execute(query)

            # Obtener los nombres de las columnas
            columnas = [desc[0] for desc in cursor.description]

            # Obtener los registros
            registros = cursor.fetchall()

            # Convertir los registros a un DataFrame de pandas
            df = pd.DataFrame(registros, columns=columnas)

            # Mostrar el DataFrame
            print("Registros consultados':")
            print(df)

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        # Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

# Llamar a la función para obtener los registros avanzados
obtener_registros_avanzados()