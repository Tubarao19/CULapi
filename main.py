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
        raise HTTPException(status_code=500, detail=f"error al conectar con mysql {err}")
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
    except ValueError as e:  # los datos entregados de forma erronea o tipo erroneo
        raise HTTPException(status_code=403 ,detail=f"Error dato incorrecto {e}")
    finally:
        cursor.close()

@app.put('/user/{id}')  # se crea solo user porque se actualizara uno y se debe mandar id del usuario a actulizar
async def create_user(user:User, id: int):# recibir el id de tipo entero
    cursor = connection.cursor()
    query = "UPDATE users (username, password) VALUES (%s, %s) where id = %i" # se actualizan los datos donde el id sea igual
    values = (user.username, user.password, id)

    try:
        cursor.execute(query,values)
        connection.commit()  #donde se empieza a guardar info en la bd
        return {"message":"usuario actualizado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"error al guardar el usuario {err}")
    except ValueError as e:  # los datos entregados de forma erronea o tipo erroneo
        raise HTTPException(status_code=403 ,detail=f"Error dato incorrecto {e}")
    finally:
        cursor.close()

@app.delete('/user/{id}')  # se crea solo user porque se actualizara uno y se debe mandar id del usuario a actulizar
async def create_user(id: int):# recibir el id de tipo entero
    cursor = connection.cursor()
    query = "DELETE from users where id = %i" # se eliminan los datos donde el id sea igual
    values = (id)

    try:
        cursor.execute(query,values)
        connection.commit()  #donde se empieza a guardar info en la bd
        return {"message":"usuario eliminado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"error al guardar el usuario {err}")
    except ValueError as e:  # los datos entregados de forma erronea o tipo erroneo
        raise HTTPException(status_code=403 ,detail=f"Error dato incorrecto {e}")
    finally:
        cursor.close()