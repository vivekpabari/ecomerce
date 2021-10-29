import datetime
from sqlalchemy import Column , String , Boolean , Integer , DateTime
from sqlalchemy.sql import func

from db.database import Base


class Product(Base):
    __tablename__ = "product"
    product_id = Column(Integer , primary_key = True)
    product_name = Column(String)
    product_model = Column(String)
    category_id = Column(String)
    company_id = Column(Integer)
    price = Column(Integer)
    feature = Column(String())
    lanch_date = Column(DateTime)
    is_active = Column(Boolean(), default=True)
    quantity = Column(Integer)
    time_created = Column(DateTime() , default = func.now())
    time_updated = Column(DateTime() , default = func.now())

