from pydantic import BaseModel,Field
from datetime import date
from typing import List,Optional

class Product(BaseModel):
    product_name: str #= Field(...,max_length=75,min_length=3)
    product_model:str 
    category_id:str = Field(...,max_length=32,min_length=32) #doubt
    company_id:int #doubt
    price:int = Field(...,gt=0,le=10**7)
    lanch_date:Optional['date'] = None #Date pydantic model
    feature:str = Field(...,max_length=250,min_length=10)


class Product_Add(Product):
    quantity:int


class ProductList(BaseModel):
    __root__ : List[Product]
