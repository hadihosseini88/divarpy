import configurations.base_db as base_db
from configurations.base_db import DatabaseConfiguration, start_db
from .models import Product, UpdateProduct
from bson.objectid import ObjectId


class Database(DatabaseConfiguration):
    @start_db()
    async def get_all_products(self):
        query = base_db.client.product_collection.find()
        product_list = []
        async for product in query:
            product["_id"] = str(product["_id"])
            product_list.append(product)
        return product_list

    @start_db()
    async def get_product(self, product_id):
        query = await base_db.client.product_collection.find_one(
            {"_id": ObjectId(product_id)}
        )
        query["_id"] = str(query["_id"])
        return query

    @start_db()
    async def create_product(self, product: Product):
        query = await base_db.client.product_collection.insert_one(product.dict())
        return str(query.inserted_id)

    @start_db()
    async def update_product(self, product_id, product: Product):
        query = await base_db.client.product_collection.update_one(
            {"_id": ObjectId(product_id)}, {"$set": product.dict()}
        )
        return query.modified_count

    @start_db()
    async def partial_update_product(self, product_id, product: UpdateProduct):
        product_update = {}
        for key in product.dict():
            if product.dict()[key]:
                product_update[key] = product.dict()[key]
        query = await base_db.client.product_collection.update_one(
            {"_id": ObjectId(product_id)}, {"$set": product_update}
        )
        return query.modified_count

    @start_db()
    async def delete_product(self, product_id):
        query = await base_db.client.product_collection.delete_one(
            {"_id": ObjectId(product_id)}
        )
        return query.deleted_count
