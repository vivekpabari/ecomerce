from pydantic import Field , BaseModel,validator

class abc(BaseModel):
    name:str = Field(...,min_length=2,max_length=100,regex="^[a-zA-Z]+([a-zA-Z\&\-\_\,\'\.\s]+)?$")
    mobile:str = Field(...,min_length=7,max_length=14,regex="^[\+]?[0-9\s\-]+$")

try:
    test = [0]*5
    test[1] = abc(name="vivek",mobile=97525787)
    test[2] = abc(name="vivek erkjgke 's _ - .  &",mobile=97525787)

    test[3] = abc(
        name="viv88ek",
        mobil=97525787
    )

    test[4] = abc(
        name="viveknnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",
        mobile=97525787
    )
    test[0] = abc(
        name="vivek",
        mobile=97525787
    )
    for i in range(5):
        print(test[i])
except ValidationError:
    print("error")