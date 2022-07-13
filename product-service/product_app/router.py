from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .db import Database
from .models import Product, UpdateProduct

router = InferringRouter()
db_client = Database()


@cbv(router)
class ProductRouter:
    @router.get("/")
    async def get_all_products(self):
        return await db_client.get_all_products()

    @router.get("/{product_id}")
    async def get_product(self, product_id):
        return await db_client.get_product(product_id)

    @router.post("/")
    async def create_product(self, product: Product):
        return await db_client.create_product(product)

    @router.put("/{product_id}")
    async def update_product(self, product_id, product: Product):
        return await db_client.update_product(product_id, product)

    @router.patch("/{product_id}")
    async def patch_product(self, product_id, product: UpdateProduct):
        return await db_client.partial_update_product(product_id, product)

    @router.delete("/{product_id}")
    async def delete_product(self, product_id):
        return await db_client.delete_product(product_id)
