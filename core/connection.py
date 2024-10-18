import mysql.connector

#diccionario con la conexion a mysql
mysql_config = {
    'host':'localhost',
    'user':'root',
    'database':'api',
    'password':'123456',
    'auth_plugin':'mysql_native_password'#se especifica el tipo de conexion
}

#para no tener que describir todas las propiedades de mysql_config se le pone 
# los dos **, para que la funcion misma lo descomponga
connection = mysql.connector.connect(**mysql_config)

def get_connection():
    return connection