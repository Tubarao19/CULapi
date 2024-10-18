from fastapi import FastAPI, HTTPException
import mysql.connector
from core.connection import connection
from models.user import User

app = FastAPI()

@app.get('/')
def root():
    return {"message":"hello world"}

@app.get('/users')#se consultan varios usuarios por eso el plural
async def get_users():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users"

    try: #intentar
        cursor.execute(query)#se queda en memoria del server de mysql
        users = cursor.fetchall()  # traer todo los registros que se pidan arriba y lo guarde en users
        return users
    except mysql.connector.Error as err: #  excepciones son errores donde se hace referencia a un alias osea err
        raise HTTPException(status_code=500, detail="error al conectar con mysql")
    finally:
        cursor.close()

@app.post('/user')  # se crea solo user porque solo lo subira un usuario
async def create_user(user:User):
    cursor = connection.cursor()  # se crea solamente el cursor para conectarse a la bd
    query = "INSERT INTO users (username, password) VALUES (%s, %s)" # se insertan los datos a la bd
    values = (user.username, user.password)

    try:
        cursor.execute(query,values)
        connection.commit()  #donde se empieza a guardar info en la bd
        return {"message":"usuario creado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"error al guardar el usuario {err}")
    except ValueError as e:
        raise 