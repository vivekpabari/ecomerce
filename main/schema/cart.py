from typing import List

from pydantic import BaseModel

#we can send timestamp with this

class Cart(BaseModel):
    #user:int
    product_id:int
    quantity:int

class CartList(BaseModel):
    __root__ : List[Cart]
