from fastapi import APIRouter , Depends , HTTPException
from fastapi.encoders import jsonable_encoder
from typing import Optional


from schema.address import AddressAdd,AddressList
from crud.curd_address import Address_create,GetByUserId,GetByAddressId, DeleteAddressById
from db.database import SessionLocal
from auth.auth_bearer import JWTBearer

route = APIRouter(prefix="/address" , tags = ["Address"])

@route.get('/test')
def test():
   return "pass"

@route.post("/add" , status_code = 201,)
def addressadd(address:AddressAdd , current_user = Depends(JWTBearer())):
    address = jsonable_encoder(address)
    
    Address_create(address , current_user)
    return "Address Added Successful"

@route.get("/user"  , response_model = AddressList , status_code = 200 )
def get_address_by_user_id(
    current_user:int = Depends(JWTBearer()),
    limit:Optional[int] = None,
    skip:Optional[int] = None,):
    address = GetByUserId(current_user , limit , skip)
    return address

@route.get("/{id}" , response_model = AddressAdd, status_code = 200 )
def get_address_by_id(id:int , current_user = Depends(JWTBearer())):
    address = GetByAddressId(id )
    if address['user_id'] != current_user:
        raise HTTPException(status_code = 403 , detail= "forbidden" ) 
    return address

@route.delete("/delete/{id}" , status_code = 200)
def delete_address_by_id(id:int , current_user = Depends(JWTBearer())):
    DeleteAddressById(id,current_user)
    return "Done"
