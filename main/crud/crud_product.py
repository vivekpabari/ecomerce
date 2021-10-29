from fastapi import HTTPException
from sqlalchemy.dialects.mysql import match
from sqlalchemy.sql import select , text 


from db.database import SessionLocal
from db.model.db_product import Product


"""
Product which is not active will not return
"""






def ProductAdd(product):
    db = SessionLocal()
    product = Product(**product)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def GetProductById(id):
    db = SessionLocal()
    product = db.query(Product).filter_by(product_id = id).first()
    if  not product or product.is_active == 0:
        raise HTTPException(status_code = 404 , detail= "Not Found")
    return product.__dict__


def GetProductByCompanyId(id , v , limit , offset , sortby , sortorder , *arg):
    db = SessionLocal()
    if v:
        t = text(f"SELECT * FROM product WHERE company_id = {id} AND is_active = 1 AND MATCH (product_name) AGAINST (:a IN BOOLEAN MODE) ORDER BY {sortby} {sortorder} LIMIT {limit} OFFSET {offset};")
        product = db.execute(t , {"a":arg[0]+"*"}).fetchall()
    else:
        t = text(f"SELECT * FROM product WHERE company_id = {id} AND is_active = 1 ORDER BY {sortby}  {sortorder} LIMIT {limit} OFFSET {offset};")
        product = db.execute(t).fetchall()
    
    if  not product:
        raise HTTPException(status_code = 404 , detail= "Not Found")
    result = [dict(row) for row in product]
    return result
    # db = SessionLocal()
    # product = db.query(Product).filter_by(company_id = id).limit(limit).offset(skip).all()
    # if  not product :
    #     raise HTTPException(status_code = 404 , detail= "Not Found")
    # listproduct = []
    # for i in product:
    #     if i.is_active == 0:
    #         continue
    #     listproduct.append(i.__dict__)
    # return listproduct


#def GetProductByCategoryId(id , limit , skip):
def GetProductByCategoryId(id , v , limit , offset , sortby , sortorder , *arg):
    db = SessionLocal()
    if v:
        t = text(f"SELECT * FROM product WHERE category_id = :id AND is_active = 1 AND MATCH (product_name) AGAINST (:a IN BOOLEAN MODE) ORDER BY {sortby} {sortorder} LIMIT {limit} OFFSET {offset};")
        product = db.execute(t , {"a":arg[0]+"*" , "id":id}).fetchall()
    else:
        t = text(f"SELECT * FROM product WHERE category_id = :id  AND is_active = 1 ORDER BY {sortby}  {sortorder} LIMIT {limit} OFFSET {offset};")
        product = db.execute(t , {"id":id}).fetchall()
    
    if  not product:
        raise HTTPException(status_code = 404 , detail= "Not Found")
    result = [dict(row) for row in product]
    return result
    # db = SessionLocal()
    # product = db.query(Product).filter_by(category_id = id).limit(limit).offset(skip).all()
    # if  not product:
    #     raise HTTPException(status_code = 404 , detail= "Not Found")
    # listproduct = []
    # for i in product:
    #     if i.is_active == 0:
    #         continue
    #     listproduct.append(i.__dict__)
    # return listproduct


def DeleteProductById(id):
    db = SessionLocal()
    product = db.query(Product).filter_by(product_id = id).first()
    if  not product:
        raise HTTPException(status_code = 404 , detail= "Not Found")
    product.is_active = 0
    db.commit()
    return "Done"

def SearchProductByString(v:str , limit , offset , sortby , sortorder):
    db = SessionLocal()
    t = text("SELECT * FROM product WHERE MATCH (product_name) AGAINST (:a IN BOOLEAN MODE) LIMIT :limit OFFSET :offset ORDER BY :sortby :sortorder;")
    product = db.execute(t , {"a":v + "*" , "limit":limit , "offset":offset , "sortby":sortby , "sortorder":sortorder}).fetchall()
    if  not product:
        raise HTTPException(status_code = 404 , detail= "Not Found")
    result = [dict(row) for row in product]
    # print(result)
    # listproduct = []
    # for i in result:
    #     listproduct.append(i['Product'].__dict__)
    # listproduct = []
    # d, a = {}, []
    # for rowproxy in product:
    #     for column, value in rowproxy.items():
    #         d = {**d, **{column: value}}
    #     a.append(d)
    return result
    
