from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

class Product(BaseModel):
    productId: str
    productName: str
    price: int
    onOffer: Union[bool, None] = None

app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None,v: Union[str,None] = None):
    return {"item_id": item_id, "q": q, "v": v}

@app.put("/product/{productNumber}")
async def addNewProduct(productNumber: int,product: Product):
    return {"productNumber":productNumber,"product":product}