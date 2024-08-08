import mysql.connector
from mysql.connector import Error

def insertar_registro(tabla, columnas, valores):
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

            # Crear la consulta SQL para insertar el registro
            columnas_str = ", ".join(columnas)
            valores_placeholder = ", ".join(["%s"] * len(valores))
            query = f"INSERT INTO curso VALUES (20, 'Especial', 30);"

            # Ejecutar la consulta de inserción
            cursor.execute(query)

            # Confirmar los cambios en la base de datos
            connection.commit()

            print("Registro insertado exitosamente.")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        # Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

# Ejemplo de uso: insertar un registro en una tabla llamada 'curso'
nombre_tabla = "curso"
columnas = ["nombre", "nivel", "duracion"]
valores = ("Curso de Python", "Intermedio", "30 horas")

# Llamar a la función para insertar el registro
insertar_registro(nombre_tabla, columnas, valores)