from fastapi import HTTPException
from typing import Dict


from db.model.db_address import Address
from db.database import SessionLocal

def Address_create(address,user):
    db = SessionLocal()
    db_address = Address(user_id = user , **address)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def GetByUserId(id:int , limit:int , skip:int):
    db = SessionLocal()
    listaddress = db.query(Address).filter_by(user_id = id).limit(limit).offset(limit).all()
    li = []
    for ele in listaddress:
        if ele.is_active == 0:
            continue
        li.append(ele.__dict__)
    return li

def GetByAddressId(id:int) -> Dict:
    db = SessionLocal()
    address = db.query(Address).filter_by(address_id = id).first()
    if not address or address.is_active == 0:
        raise HTTPException(status_code=404 , detail="NOt Found")
    return address.__dict__


def DeleteAddressById(id:int , user_id:int) -> str:
    db = SessionLocal()
    address = db.query(Address).filter_by(address_id = id , user_id = user_id).first()
    if not address or address.is_active == 0:
        raise HTTPException(status_code=404 , detail="NOt Found")
    address.is_active = 0
    db.commit()
    return "Done"
