from typing import Union,Dict,List
import logging
from fastapi import HTTPException


from db.model.db_order import Order , OrderProduct
from db.database import SessionLocal

def AddOrder(order):
    try:
        db = SessionLocal()
        order = Order(**order)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order.order_id
    except Exception as err:
        logging.error(err)


def AddProductIdOrder(order_id,product_id,quantity):
    try:
        db = SessionLocal()
        for i,j in zip(product_id,quantity):
            orderproduct = OrderProduct(order_id = order_id , product_id = i, quantity = j)
            db.add(orderproduct)
            db.commit()
            db.refresh(orderproduct)
        return "Added"
    except Exception as err:
        logging.error(err)

def GetOrderById(id:int , user_id:int) -> Union[Dict,None]:
    db = SessionLocal()
    order = db.query(Order).filter_by(order_id = id , user_id = user_id).first()
    if not order:
        raise HTTPException(status_code=404 , detail= "Not Found")
    return order.__dict__


def GetOrderProductById(id:int) -> Union[List,None]:
    db = SessionLocal()
    orderproduct = db.query(OrderProduct).filter_by(order_id = id).all()
    product_id_list = []
    quantity_list = []
    for i in orderproduct:
        product_id_list.append(i.product_id)
        quantity_list.append(i.quantity)
    return product_id_list,quantity_list


def GetOrderByUser(id:int , limit:int , skip:int) -> Union[List[Dict],None]:
    db = SessionLocal()
    order = db.query(Order).filter_by(user_id = id).limit(limit).offset(limit).all()
    if not order:
        return None
    listorder = []
    for i in order:
        temp = i.__dict__
        temp["product_id"] , temp["quantity"] = GetOrderProductById(temp['order_id'])
        listorder.append(temp)
    return listorder


# def DeleteOrderById(id:int , current_user:int) -> str:
#     db = SessionLocal()
#     order = db.query(Order).filter_by(order_id = id , user_id = user_id).first()
#     if not order or order.is_active == 0:
#         raise HTTPException(status_code=404 , detail= "Not Found")
#     order.is_active = 0
#     db.commit()
#     return "done"
    