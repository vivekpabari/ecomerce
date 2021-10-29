from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder


from schema.company import CompanySchema , CompanyListSchema
from crud.crud_company import AddCompany , GetCompanyById


route = APIRouter(prefix="/company" , tags= ["Company"])


@route.get("/get/{id}" , status_code = 200 , response_model = CompanySchema)
def get_category_by_id(id:int):
    category = GetCompanyById(id) 
    return category


@route.post("/add" , status_code = 201 )
def add_company(company:CompanySchema):
    company = jsonable_encoder(company)
    AddCompany(company)
    return "Add Successfully"