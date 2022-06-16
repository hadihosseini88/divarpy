from fastapi.testclient import TestClient
from main import app
import time
from .test_setup import TestSetup

test_client = TestClient(app)

class TestRouter(TestSetup):
    def test_user_can_product(self):
        query =self.create_fake_product()
        response = test_client.get("/")
        response = response.json()
        assert response[-1]["_id"] == str(query.inserted_id)
        assert response[-1]["name"] == self.fake_product["name"]

    def test_user_can_create_product(self):
        del self.fake_product["_id"]
        response = test_client.post("/", json=self.fake_product)
        response = response.json()
        assert self.get_product(response)["name"] == self.fake_product["name"]

    def test_user_can_update_product(self):
        query = self.create_fake_product()
        del self.fake_product["_id"]
        response = test_client.put(
            f"/{query.inserted_id}", json=self.fake_product
        )
        response = response.json()
        assert response == 1

    def test_user_can_partial_update_product(self):
        query = self.create_fake_product()
        del self.fake_product["_id"]
        del self.fake_product["description"]
        response = test_client.patch(
            f"/{query.inserted_id}", json=self.fake_product  
        )
        response = response.json()
        assert response == 1

    def test_user_can_delete_product(self):
        query = self.create_fake_product()
        test_client.delete(f"/{query.inserted_id}")
        time.sleep(0.01)
        product = self.get_product(query.inserted_id)
        assert not product