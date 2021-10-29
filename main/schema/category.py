from pydantic import BaseModel , Field
from typing import Optional , List


class CategorySchema(BaseModel):
    category_id:str = Field(...,max_length=32,min_length=32)
    category_name:str
    parent_id:Optional[str]


class CategoryListSchema(BaseModel):
    __root__:List[CategorySchema]