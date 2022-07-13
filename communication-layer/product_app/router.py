from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .http_service import ProductHttpService
from .model import Product, UpdateProduct

router = InferringRouter()
http_service = ProductHttpService()


@cbv(router)
class ProductRouter:
    @router.get("/")
    async def get_products(self):
        return await http_service.get_products()

    @router.get("/{product_id}")
    async def get_product(self, product_id: str):
        return await http_service.get_product(product_id)

    @router.post("/")
    async def create_product(self, product: Product):
        return await http_service.create_product(product)

    @router.put("/{product_id}")
    async def update_product(self, product_id: str, product: Product):
        return await http_service.update_product(product_id, product)

    @router.patch("/{product_id}")
    async def partial_update_product(self, product_id: str, product: UpdateProduct):
        return await http_service.partial_update_product(product_id, product)
    
    @router.delete("/{product_id}")
    async def delete_product(self, product_id: str):
        return await http_service.delete_product(product_id)