from pydantic import Field,BaseModel
from typing import Optional,List

class AddressAdd(BaseModel):
    line_1:str = Field(...,min_length=6 , max_length=70)
    line_2:Optional['str'] = None
    city:str = Field(..., max_length=35 , min_length=3)
    pincode:int = Field(...,ge=100000,le=999999)
    country:str = Field(..., max_length=35 , min_length=3)

class AddressList(BaseModel):
    __root__ : List[AddressAdd]