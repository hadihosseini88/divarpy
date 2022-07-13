import requests
from settings import get_settings
from .model import Product, UpdateProduct

settings = get_settings()


class ProductHttpService:
    product_service_url: str

    def __init__(self):
        self.product_service_url = settings.product_service_url

    async def get_products(self):
        request = requests.get(
            f"{self.product_service_url}/",
        )
        return request.json()

    async def get_product(self, product_id: str):
        request = requests.get(
            f"{self.product_service_url}/{product_id}",
        )
        return request.json()

    async def create_product(self, product: Product):
        request = requests.post(
            f"{self.product_service_url}/",
            json=product.dict(),
        )
        return request.json()

    async def update_product(self, product_id: str, product: Product):
        request = requests.put(
            f"{self.product_service_url}/{product_id}",
            json=product.dict(),
        )
        return request.json()

    async def partial_update_product(self, product_id: str, product: UpdateProduct):
        request = requests.patch(
            f"{self.product_service_url}/{product_id}",
            json=product.dict(),
        )
        return request.json()

    async def delete_product(self, product_id: str):
        request = requests.delete(
            f"{self.product_service_url}/{product_id}",
        )
        return request.json()
