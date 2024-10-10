from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    password: str 

@app.get('/')
def read_root():
    return {"nombre":"Miguel", "edad":27}

@app.get('/users')
def list_users():
    return [
        {
        'name':'berim',
        'email':'berim@gmail.com'
        },
        {
        'name':'leo',
        'email':'leo@gmail.com'
        }
    ]

@app.post('/login')
def login(dato:User):
    if(dato.email == 'miguel@test.com' and dato.password == '1234'):
        return{
            'status':'success',
            'message':'datos correctos',
            'data':{
                'user_id':1
            }
        }
    else:
        return{
            'status':'error',
            'message':'verifique usuario y contraseña'
        }