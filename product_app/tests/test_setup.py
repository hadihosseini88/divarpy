from bson import ObjectId
from configurations.base_test import TestConfiguration

class TestSetup(TestConfiguration):
    fake_product = {
        "name": "test name",
        "description": "test address", 
        "price": 100.00,
    }

    def create_fake_product(self):
        return self.product_collection.insert_one(self.fake_product)

    def get_product(self, product_id):
        return self.product_collection.find_one({"_id": ObjectId(product_id)})

