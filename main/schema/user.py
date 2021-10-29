from pydantic import BaseModel,Field,validator,EmailStr,ValidationError

from crud.curd_user import get_user


class SignUp(BaseModel):
    first_name:str
    middle_name:str 
    last_name:str
    email:EmailStr #Field(...,regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    password:str = Field(...,min_length=8,max_length=20)
    mobile_number:int = Field(...,gt=10**9,le=9999999999)

    @validator('email')
    def email_not_present(cls , v):
        #check in database if email is present or not
        user = get_user(v)
        if user:
            raise ValueError("User Already Exist")
        return v
        

class Login(BaseModel):
    email:EmailStr
    password:str = Field(...,min_length=8,max_length=20)

class ResetPassword(BaseModel):
    email: str = Field(...,regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    password1: str = Field(...,min_length=8,max_length=20)
    password2: str = Field(...,min_length=8,max_length=20)

    @validator('password2')
    def chech_password1_isequal_password2(cls , v):
        if v!=password1:
            raise ValueError('passwords do not match')
        return v
    