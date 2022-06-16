from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: float

class UpdateProduct(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = 0
