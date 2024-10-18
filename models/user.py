from pydantic import BaseModel

class User(BaseModel):#extiende el basemodel de su clase basemodel 
    username: str
    password: str