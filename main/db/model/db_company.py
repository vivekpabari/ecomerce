from sqlalchemy import Column  , Integer , String  


from db.database import Base

class Company(Base):
    __tablename__ = "company"
    company_id = Column(Integer , primary_key = True)
    company_name = Column(String , nullable = False)
    company_detail = Column(String , nullable = True)
    company_category = Column(String , nullable = False)