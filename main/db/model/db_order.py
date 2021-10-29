from sqlalchemy import Column , DateTime , Integer , String , Float 
from sqlalchemy.sql import func



from db.database import Base




class Order(Base):
    __tablename__ = "order"
    order_id = Column(Integer , primary_key = True)
    user_id = Column(Integer , nullable = False)
    address_id = Column(Integer , nullable = False)
    payment_id = Column(Integer , default = 0)
    total_bill = Column(Float(precision=2) , nullable = False)
    status = Column(String)
    time_created = Column(DateTime , default = func.now())
    time_updated = Column(DateTime , default = func.now())

class OrderProduct(Base):
    __tablename__ = "orderproduct"
    order_id = Column(Integer ,primary_key=True ,nullable = False)
    product_id = Column(Integer ,primary_key=True, nullable = False)
    quantity = Column(Integer , nullable = False)