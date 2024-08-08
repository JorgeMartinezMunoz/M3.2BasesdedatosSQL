import mysql.connector
import pandas as pd
from mysql.connector import Error

def exportar_tabla_a_excel():
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

            # Consultar todos los registros de la tabla 'curso'
            query = "SELECT * FROM asignatura where idAsignatura > 'AS004';"
            cursor.execute(query)

            # Obtener los nombres de las columnas
            columnas = [desc[0] for desc in cursor.description]

            # Obtener los registros
            registros = cursor.fetchall()

            # Convertir los registros a un DataFrame de pandas
            df = pd.DataFrame(registros, columns=columnas)
            print(df)

            # Exportar el DataFrame a un archivo Excel
            df.to_excel('cursos.xlsx', index=False, engine='openpyxl')
            print("Datos exportados exitosamente a 'cursos.xlsx'.")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        # Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

# Llamar a la función para exportar la tabla a Excel
exportar_tabla_a_excel()