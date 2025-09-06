import allure

from api.base_api import ApiClient


class StoreApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def get_inventory(self):
        with allure.step("GET /store/inventory"):
            return self.client.get("/store/inventory")

    def get_info_about_placed_order_by_id(self, order_id: int):
        with allure.step(f"GET /store/order/{order_id}"):
            return self.client.get(f"/store/order/{order_id}")

    def place_order(self, body:dict):
        with allure.step("POST /store/order"):
            return self.client.post("/store/order", body)

    def delete_placed_order(self, order_id: int):
        with allure.step(f"DELETE /store/order/{order_id}"):
            return self.client.delete(f"/store/order/{order_id}")