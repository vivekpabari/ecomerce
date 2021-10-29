from fastapi import FastAPI , HTTPException , Depends
import uvicorn

from apis import user,product,address,order,cart , category , company

app = FastAPI()

app.include_router(user.route)
app.include_router(product.route)
app.include_router(address.route)
app.include_router(order.route)
app.include_router(cart.route)
app.include_router(category.route)
app.include_router(company.route)


@app.get("/test")
def test():
    return "Pass"



@app.get("/")
def index():
    return "Do Your Best"

if __name__ == "__main__":
    uvicorn.run("main:app" , port=8050 , reload = True)