from sqlalchemy import Column , String , Integer

from db.database import Base

class Cart(Base):
    __tablename__ = "cart"
    cart_id = Column(Integer , primary_key = True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    status = Column(Integer , default = 1)