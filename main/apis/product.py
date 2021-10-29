from fastapi import APIRouter,Query,Path
from fastapi.encoders import jsonable_encoder
from typing import Optional


from schema.product import Product_Add , Product , ProductList
from schema.request_body import PaginationRequest
from schema.response_body import ResponseBody
from crud.crud_product import ProductAdd , GetProductById , GetProductByCompanyId , GetProductByCategoryId , DeleteProductById , SearchProductByString
from datetime import date


route = APIRouter(prefix="/product" , tags=['Product'])


def response_body_syntax(payload , pager , status = 200 , message = "Successful"):
    d = {
        "status":status , 
         "message":message,
         "payload":payload,
         "pager":pager
        }
    return d


@route.post("/search/{text}", response_model = ProductList , status_code = 200)
def product_search(text:str, request:PaginationRequest):
    request = jsonable_encoder(request)
    if request["showall"]:
        request['recordsperpage'] = 18446744073709551615
        request['rownumber'] = 0
    else:
        request['rownumber'] *= request['recordsperpage'] 
    product = SearchProductByString(text , request['recordsperpage'] ,request['rownumber'] )
    return product


@route.post("/product/add", status_code = 201 )
def productadd(item:Product_Add):
    product = jsonable_encoder(item)
    ProductAdd(product)
    return "Product add successfully"


@route.get("/view/{id}", response_model = Product , status_code = 200 )
def productview(
    id:int = Path(...,title="ID of the product")):
    #call for data
    product = GetProductById(id)
    return product


@route.post("/companyid/{id}" , response_model = ResponseBody , status_code = 200 )
def productviewbycompany(
    request:PaginationRequest,
    id:int = Path(...,title="ID of the product"),
    ):
    request = jsonable_encoder(request)
    if request["showall"]:
        request['recordsperpage'] = 18446744073709551615
        request['rownumber'] = 0
    else:
        request['rownumber'] *= request['recordsperpage']
    d = request['search']
    
    if d['filter']:
        product = GetProductByCompanyId(id , True , request['recordsperpage'] ,request['rownumber'] , request['sortby'] , request['sortorder'] , d['text'])
    else:
        product = GetProductByCompanyId(id , False , request['recordsperpage'] ,request['rownumber'] , request['sortby'] , request['sortorder'] )
    return response_body_syntax(product , request)


@route.post("/categoryid/{id}" , response_model = ResponseBody , status_code = 200 )
def productviewbycompany(
    request:PaginationRequest,
    id:str = Path(...,title="ID of the company"),
    ):
    request = jsonable_encoder(request)
    if request["showall"]:
        request['recordsperpage'] = 18446744073709551615
        request['rownumber'] = 0
    else:
        request['rownumber'] *= request['recordsperpage']
    d = request['search']
    
    if d['filter']:
        product = GetProductByCategoryId(id , True , request['recordsperpage'] ,request['rownumber'] , request['sortby'] , request['sortorder'] , d['text'])
    else:
        product = GetProductByCategoryId(id , False , request['recordsperpage'] ,request['rownumber'] , request['sortby'] , request['sortorder'] )
    return response_body_syntax(product , request)


@route.delete("delete/{id}" , status_code = 200)
def productdeletebyid(
    id:int
    ):
    DeleteProductById(id)
    return "Done"
