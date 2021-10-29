from typing import Union,Dict,List
import logging
from fastapi import HTTPException


from db.model.db_company import Company
from db.database import SessionLocal


def AddCompany(company):
    try:
        db = SessionLocal()
        company = Company(**company)
        db.add(company)
        db.commit()
        db.refresh(company)
    except Exception as err:
        logging.error(err)
        company = None
    return company


def GetCompanyById(id:int) -> Dict:
    db = SessionLocal()
    company = db.query(Company).filter_by(company_id = id).one()
    if not company:
        raise HTTPException(status_code=404 , detail="Company Not Found")
    return company.__dict__
