from fastapi import APIRouter , Depends , HTTPException
from fastapi.encoders import jsonable_encoder
from typing import Optional


from schema.cart import Cart , CartList
from auth.auth_bearer import JWTBearer
from crud.crud_cart import CartAdd , GetCartByUserId , GetCartById , DeleteCartById

route = APIRouter(prefix="/cart" , tags= ['Cart'] )




@route.get("/test")
def test():
    return "pass"


@route.post("/cartadd")
def cart_add(cart:Cart , current_user = Depends(JWTBearer())):
    cart = jsonable_encoder(cart)
    CartAdd(cart , current_user)
    return "successful"

@route.get("/view/{id}" , status_code = 200 , response_model = Cart)
def cart_view_by_id(id:int , current_user = Depends(JWTBearer())):
    cart = GetCartById(id,current_user)
    return cart


@route.get("/viewbyuser" , status_code = 200 , response_model = CartList)
def cart_view_by_id(
    current_user = Depends(JWTBearer()),
    limit:Optional[int] = None,
    skip:Optional[int] = None,):
    cart = GetCartByUserId(current_user , limit , skip)
    return cart


@route.delete("/delete/{id}" , status_code = 200)
def cart_delete_by_id(
    id:int , 
    current_user = Depends(JWTBearer()),
    ):
    DeleteCartById(id , current_user)
    return "Done"