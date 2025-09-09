import allure

from api.base_api import ApiClient


class PetApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def add_pet(self,pet_body:dict):
        with allure.step("POST /pet"):
            return self.client.post("/pet",body=pet_body)

    def update_pet(self,pet_body:dict):
        with allure.step("PUT /pet"):
            return self.client.put("/pet",body=pet_body)

    def find_pet_by_status(self,status="available"):
        with allure.step("GET /pet/findByStatus"):
            return self.client.get(f"/pet/findByStatus?status={status}")
