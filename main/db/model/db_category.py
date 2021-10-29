from sqlalchemy import Column , DateTime , Integer , String , Float 


from db.database import Base

class Category(Base):
    __tablename__ = "category"
    category_id = Column(String , primary_key = True)
    category_name = Column(String , nullable = False)
    parent_id = Column(String)