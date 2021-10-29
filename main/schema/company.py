from pydantic import BaseModel , Field
from typing import Optional , List


class CompanySchema(BaseModel):
    company_name:str
    company_detail:Optional[str]
    company_category:str = Field(...,max_length=32,min_length=32)


class CompanyListSchema(BaseModel):
    __root__:List[CompanySchema]