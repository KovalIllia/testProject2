# import datetime
# import random
#
# import allure
# import requests
#
#
# class ApiClient:
#     base_url = "https://petstore.swagger.io/v2"
#
#     def __init__(self, logger):
#         self.logger = logger
#
#     def build_url(self, resource: str) -> str:
#         return f"{self.base_url}{resource}"
#
#     def get(self, resource: str, params: dict = None) -> requests.Response:
#         url = self.build_url(resource)
#         self.logger.add_request(url, method="GET", body=params)
#         response = requests.get(url)
#         self.logger.add_response(response, body=params)
#         return response
#
#     def post(self, resource: str, body: dict)->requests.Response:
#         url = self.build_url(resource)
#         self.logger.add_request(url, method="POST", body=body)
#         response = requests.post(url, json=body)
#         self.logger.add_response(response, body=body)
#         return response
#
#     def delete(self, resource: str, params: dict = None) -> requests.Response:
#         url = self.build_url(resource)
#         self.logger.add_request(url, method="DELETE", body=params)
#         response = requests.delete(url)
#         self.logger.add_response(response, body=params)
#         return response
#
#
# class StoreApi:
#
#     def __init__(self, client: ApiClient):
#         self.client = client
#
#     def get_inventory(self):
#         with allure.step("GET /store/inventory"):
#             return self.client.get("/store/inventory")
#
#     def get_info_about_placed_order_by_id(self, order_id: int):
#         with allure.step(f"GET /store/order/{order_id}"):
#             return self.client.get(f"/store/order/{order_id}")
#
#     def place_order(self, body:dict):
#         with allure.step("POST /store/order"):
#             return self.client.post("/store/order", body)
#
#     def delete_placed_order(self, order_id: int):
#         with allure.step(f"DELETE /store/order/{order_id}"):
#             return self.client.delete(f"/store/order/{order_id}")
#
#
# class PetApi:
#
#     def __int__(self, client: ApiClient):
#         self.client = client
#
#     def add_pet(self,pet_body:dict):
#         with allure.step("POST /pet"):
#             return self.client.post("/pet",body=pet_body)
#
