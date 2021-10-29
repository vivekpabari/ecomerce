from pydantic import BaseModel
from typing import Optional , Dict 

# {
# "search": "{\"filter\": \"Enable\"}",
# "rowNumber": 1,
# "recordsPerPage": 5,
# "sortOrder": "DESC",
# "sortBy": "name",
# "showAll": false
# }
class SearchText(BaseModel):
    filter:Optional[bool] = False
    text:Optional[str]


class PaginationRequest(BaseModel):
    search:SearchText
    rownumber:Optional[int] = 0
    recordsperpage:Optional[int] = 10
    sortorder:Optional[str] = "ASC"
    sortby:Optional[str] = "product_id"
    showall:Optional[bool] = False