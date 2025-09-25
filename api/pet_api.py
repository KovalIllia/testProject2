import allure

from api.base_api import ApiClient
from utils.enums import PetStatus

class PetApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def add_pet(self,pet_body:dict):
        with allure.step("POST /pet"):
            return self.client.post("/pet",body=pet_body)

    def update_pet(self,pet_body:dict):
        with allure.step("PUT /pet"):
            return self.client.put("/pet",body=pet_body)

    def find_pet_by_status(self,status=PetStatus):#pending/sold
        with allure.step("GET /pet/findByStatus"):
            return self.client.get(f"/pet/findByStatus?status={status.value}")

    def find_pet_by_id(self, pet_id: int):
        with allure.step("GET /pet/{petId}"):
            return self.client.get(f"/pet/{pet_id}")

    def update_pet_with_form_data(self, pet_id: int, name: str, status: str):
        with allure.step(f"POST /pet/{pet_id}"):
            body = {"name": name, "status": status}
            return self.client.post_form(f"/pet/{pet_id}", body=body)

    def delete_pet(self,pet_id:int):
        with allure.step("DELETE /pet/{petId}"):
            return self.client.delete(f"/pet/{pet_id}")

