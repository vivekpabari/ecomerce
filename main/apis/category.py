from fastapi import APIRouter


from schema.category import CategorySchema , CategoryListSchema
from crud.crud_category import GetCategoryById , GetCategoryByParentId


route = APIRouter(prefix="/category" , tags= ["Category"])

@route.get("/get/{id}" , status_code = 200 , response_model = CategorySchema)
def get_category_by_id(id:str):
    category = GetCategoryById(id) 
    return category


@route.get("/getbyparentid/{id}" , status_code = 200 , response_model = CategoryListSchema)
def get_category_by_id(id:str):
    category = GetCategoryByParentId(id) 
    return category

    