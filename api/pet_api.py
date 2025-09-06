import allure

from api.base_api import ApiClient


class PetApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def add_pet(self,pet_body:dict):
        with allure.step("POST /pet"):
            return self.client.post("/pet",body=pet_body)