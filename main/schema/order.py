from pydantic import BaseModel,validator,Field
from typing import List , Optional
from enum import Enum

class order_status(Enum):
    paymentpending = "Payment Pending"
    failed = "Failed"
    paymentfail = "Payment Fail"
    successful = "Successful"
    

class OrderScheme(BaseModel):
    #user_id:int 
    address_id:int
    product_id:List[int]
    quantity:List[int]
    total_bill:float
    payment_id:Optional[int] = 0
    status:order_status

class OrderSchemeList(BaseModel):
    __root__:List[OrderScheme]