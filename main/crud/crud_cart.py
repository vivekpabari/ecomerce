from typing import Union
from enum import IntEnum
from fastapi import HTTPException


from db.database import SessionLocal
from db.model.db_cart import Cart


class cart_status(IntEnum):
    added = 1
    removed = 2
    buy = 3
    
    
def CartAdd(cart , current_user):
    db = SessionLocal()
    cart = Cart(user_id = current_user , **cart)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart

def GetCartById(id , user_id):
    db = SessionLocal()
    cart = db.query(Cart).filter_by(cart_id = id, user_id = user_id).first()
    if not cart or cart.status != cart_status.added:
        raise HTTPException(status_code=404 , detail= "Not Found")
    return cart.__dict__


def GetCartByUserId(id:int , limit:Union[int,None] , skip:Union[int,None]):
    db = SessionLocal()
    cart = db.query(Cart).filter_by(user_id = id).limit(limit).offset(skip).all()
    if not cart:
        raise HTTPException(status_code=404 , detail= "Not Found")
    cartlist = []
    for i in cart:
        if i.status == cart_status.added:
            cartlist.append(i.__dict__)
    return cartlist


def DeleteCartById(id:int , current_user:int) -> str:
    db = SessionLocal()
    cart = db.query(Cart).filter_by(cart_id = id, user_id = current_user).first()
    if not cart:# or cart.status != cart_status.added:
        raise HTTPException(status_code=404 , detail= "Not Found")
    cart.status = int(cart_status.removed)
    db.commit()
    return "Done"
