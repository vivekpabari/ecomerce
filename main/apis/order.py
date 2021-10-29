from fastapi import APIRouter , Depends
from fastapi.encoders import jsonable_encoder
from typing import Optional


from auth.auth_bearer import JWTBearer
from crud.crud_order import AddOrder , AddProductIdOrder , GetOrderById , GetOrderProductById , GetOrderByUser 
from schema.order import OrderScheme , OrderSchemeList


route = APIRouter(prefix="/order" ,tags = ['Order'])

@route.get("/test")
def test():
    return "pass"
#check order total bill and address belong to user who order

@route.post("/Add", status_code = 201)
def order_add(order:OrderScheme , current_user:int = Depends(JWTBearer()) ):
    order = jsonable_encoder(order)
    order["user_id"] = current_user
    product_id = order.pop('product_id')
    quantity = order.pop('quantity')
    order_id = AddOrder(order)
    orderproduct = AddProductIdOrder(order_id , product_id , quantity)
    return "pass"

@route.get("/view/{id}" , response_model = OrderScheme , status_code = 200)
def order_view_by_id(id:int , current_user = Depends(JWTBearer())):
    order = GetOrderById(id,current_user)
    product_id , quantity = GetOrderProductById(id)
    order['product_id'] = product_id
    order['quantity'] = quantity
    return order


@route.get("/viewbyuser" , response_model = OrderSchemeList , status_code = 200)
def order_view_by_id(
    current_user = Depends(JWTBearer()),
    limit:Optional[int] = None,
    skip:Optional[int] = None):
    return  GetOrderByUser(current_user , limit , skip)

"""
You can NOT delete Order
"""

# @route.delete("/delete/{id}" , status_code = 200)
# def delete_order_by_id(
#     id:int , 
#     current_user = Depends(JWTBearer()),
#     ):
#     DeleteOrderById(id , current_user)
#     return "Done"