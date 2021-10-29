from db.database import Base

from sqlalchemy import String , Column , Integer , Boolean , DateTime
from sqlalchemy.sql import func

class Address(Base):
    __tablename__ = "address"
    address_id = Column(Integer , primary_key = True , index = True)
    user_id = Column(Integer , default = 1)#set forieg key
    line_1 = Column(String,nullable = False)
    line_2 = Column(String)
    city = Column(String)
    pincode = Column(Integer)
    country = Column(String)
    is_active = Column(Boolean , default = True)