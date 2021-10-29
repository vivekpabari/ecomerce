from fastapi import HTTPException


from db.database import SessionLocal
from db.model.db_category import Category 

def GetCategoryById(id:str):
    db = SessionLocal()
    category = db.query(Category).filter_by(category_id = id).first()
    if not category:
        raise HTTPException(status_code=404 , detail= "Category Not Found")
    return category.__dict__


def GetCategoryByParentId(id:str):
    db = SessionLocal()
    category = db.query(Category).filter_by(parent_id = id).all()
    if not category:
        raise HTTPException(status_code=404 , detail= "Category Not Found")
    categorylist = []
    for i in category:
        categorylist.append(i.__dict__)
    return categorylist