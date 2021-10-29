from typing import Generic,TypeVar
from .db.database import Base
from pydantic import BaseModel
from sqlalchemy.orm import Session


ModelType = TypeVar('ModelType',bound = Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound = BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound = BaseModel)

class CRUDBase(Generic[ModelType , CreateSchemaType , UpdateSchemaType]):
    def __init__(self,model:type[ModelType]):
        self.model = model

    def get(self):
        pass

    def multi_get(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass