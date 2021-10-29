from db.database import Base

from sqlalchemy import Boolean, Column, Integer, String , DateTime
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key = True ,index = True)
    first_name = Column(String , nullable = False)
    last_name = Column(String , nullable = False)
    middle_name = Column(String , nullable = False)
    email = Column(String , index=True , unique=True)
    mobile_number = Column(Integer)
    password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    time_created = Column(DateTime(timezone=True), default = func.now())
    time_updated = Column(DateTime(timezone=True), default = func.now())
