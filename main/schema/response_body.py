# {
#     "status": 200,
#     "message": "Password Policy List",
#     "payload": [],
#     "pager": {
#         "sortOrder": "DESC",
#         "rowNumber": 1,
#         "recordsPerPage": 5,
#         "sortBy": "name",
#         "totalRecords": 0,
#         "filteredRecords": 0
#     }
# }
from typing import Optional , Dict , Union , List
from pydantic import BaseModel , Field


from .request_body import PaginationRequest , SearchText
from .product import ProductList
class ResponseBody(BaseModel):
    status:int = Field(...,ge=100,lt=600)
    message:str
    payload:ProductList
    pager:PaginationRequest

