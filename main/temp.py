
from fastapi import FastAPI,Path,status,Body,Response,File,UploadFile
from fastapi.responses import HTMLResponse,PlainTextResponse,FileResponse
import uvicorn
from pydantic import BaseModel
from typing import Optional,List
import json
import psycopg


app = FastAPI()

conn =  psycopg.connect(dbname="test_001" , user="postgres", password="9727840182", host="localhost", port="5432")
cur = conn.cursor() 


cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')

print("Table created successfully")

conn.commit()
conn.close()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


class User(BaseModel):
    name: str 
    email: str
    password: Optional[str] = None

class UserOut(BaseModel):
    name:str
    email:str


#path parameter
@app.get("/items/{item_id}",status_code=200)
def try_1(item_id:int = Path(...,ge=100), ):
    return "Done_1"

#query and path parameter
@app.get("/try_2/{str_2}", status_code = 200)
def try_2(str_2:str,q:str):
    return json.dumps({
        "str":str_2
    })
#request body
@app.post("/add")
def add_item(item:Item,status_code = 201):
    return "Done"

#request body and query and path
@app.put("/add/{item_id}",response_model = UserOut , status_code = 201)
def add_item(
            
            q:str,
            item:Item,
            user:User,
            num:int = Body(...,embed=True),
            item_id:int = Path(...,gt=100,lt=1000),
            q_1:Optional[str] = None
            ):
    return user


@app.get("/xyz")
async def root():
    return {"message": "gyhyedrgertg"}


#display pdf
@app.get("/resume")
async def resume():
    return FileResponse("C:\\Users\\pabar\\Desktop\\027\\project\\ecomerce\\main\\vivek.pdf")


@app.get("/")
async def root():
    return {"message": "Hello World"}



if __name__ == '__main__':
    uvicorn.run("run:app", port=8050,reload = True)