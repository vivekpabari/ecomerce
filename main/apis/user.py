from fastapi import  APIRouter,Request,Response, Depends , HTTPException
from fastapi.encoders import jsonable_encoder
from schema.user import SignUp,Login
# import json
from sqlalchemy.orm import Session
from db.database import SessionLocal,engine,Base
from db.model.db_user import User
from fastapi.security import OAuth2PasswordBearer
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

route = APIRouter(prefix="/account" , tags=['Account'])

from crud.curd_user import create_user,get_user , delete_user
#from crud.crud_category import fun

@route.get('/test')
def test():
    return "pass"

@route.post("/signup" , status_code = 201 , tags = ['Account'])
async def signup(user:SignUp):
    user = jsonable_encoder(user)
    create_user(user)
    return "User Added successfully"


#check if user is activate or not ---> implemented
@route.post("/login" , status_code = 201 , tags = ['Account'])
async def login(user:Login):
    user = jsonable_encoder(user)
    db_user = get_user(user['email'])
    if not db_user or db_user['is_active'] == 0:
        raise HTTPException(404 , "User Not Found")
    if user['password'] == db_user['password']:
        token = signJWT(str(db_user['id']))
        return { 
            "message" : "Login Successfully",
            "access-token": token["access_token"]
        }
    else:
        raise HTTPException(401 , "Unauthorized")

# @route.get("/createtable")
# def createtable():
#     Base.metadata.create_all(engine)
#     return "created"

@route.delete("/deleteuser" , status_code = 204)
async def deleteuser(current_user = Depends(JWTBearer())):
    delete_user(current_user)
    return "Done"

