import datetime
import random
from http.client import responses

import requests
from utils.logger import Logger
import allure
from collections.abc import Mapping

class ApiClient:
    base_url = "https://petstore.swagger.io/v2"

    def __init__(self,logger):
        self.logger=logger

    def build_url(self, resource:str)->str:
        return f"{self.base_url}{resource}"


    def get_info_about_store(self,resource:str)-> str:
        url=self.build_url(resource)
        self.logger.add_request(url,method="GET")
        response=requests.get(url)
        self.logger.add_response(response)
        return response

    def post_store_order(self, resource: str, body: dict):
        url = self.build_url(resource)
        self.logger.add_request(url, method="POST",body=body)
        response = requests.post(url, json=body)
        self.logger.add_response(response,body=body)
        return response

    def delete_order(self,resource:str)->str:
        url=self.build_url(resource)
        self.logger.add_request(url,method="DELETE")
        response=requests.delete(url)
        return response

class StoreApi:

    def __init__(self,client: ApiClient):
        self.client=client

    def get_inventory(self):
        with allure.step("GET /store/inventory"):
            return self.client.get_info_about_store("/store/inventory")

    def get_info_about_placed_order_by_id(self, order_id:int):
        with allure.step(f"GET /store/order/{order_id}"):
            return self.client.get_info_about_store(f"/store/order/{order_id}")


    def place_order(
            self,
            id: int = None,
            petId: int = None,
            quantity: int = 1,
            shipDate: str = None,
            status: str = "placed",
            complete: bool = True):

        if id is None:
            id = random.randint(1, 10000)
        if petId is None:
            petId = random.randint(1, 10000)
        if shipDate is None:
            shipDate = datetime.datetime.now().isoformat()

        body = {
            "id": id,
            "petId": petId,
            "quantity": quantity,
            "shipDate": shipDate,
            "status": status,
            "complete": complete
        }

        with allure.step("POST /store/order"):
            return self.client.post_store_order("/store/order", body)


    def delete_placed_order(self,order_id:int):
        with allure.step(f"DELETE /store/order/{order_id}"):
            return self.client.delete_order(f"/store/order/{order_id}")







# base_url = "https://petstore.swagger.io/v2"
# logger = Logger()
#
# class Store():
#     """Access to Petstore orders"""
#
#     """Returns pet inventories by status"""
#
#     @staticmethod
#     def get_info_about_store():
#         with allure.step("GET"):
#             get_resource = "/store/inventory"
#             get_url = f"{base_url}{get_resource}"
#             result_get = requests.get(get_url)
#             Logger.add_request(result_get, method="GET")
#             Logger.add_response(result_get)
#             return result_get



    # """Place an order for a pet #1"""
    # @staticmethod
    # def place_first_order():
    #     with allure.step("POST"):
    #         post_resource = "/store/order"
    #         json_for_creat_order = {
    #         "id": 1,
    #         "petId": 1,
    #         "quantity": 1,
    #         "shipDate": "2025-06-17T19:25:58.960Z",
    #         "status": "placed",
    #         "complete": True
    #         }
    #         post_url = f"{base_url}{post_resource}"
    #         logger.add_request(post_url, method="POST")
    #         result_post=requests.post(post_url,json=json_for_creat_order)
    #         logger.add_response(result_post)
    #         return result_post
    #
    # """Place an order for a pet #2"""

    # @staticmethod
    # def store_place_order(
    #         id: int = None,
    #         petId: int = None,
    #         quantity: int = 1,
    #         shipDate: str = None,
    #         status: str = "placed",
    #         complete: bool = True):
    #
    #     if id is None:
    #         id = random.randint(1, 10000)
    #     if petId is None:
    #         petId = random.randint(1, 10000)
    #     if shipDate is None:
    #         shipDate = datetime.datetime.now().isoformat()
    #
    #     with allure.step("POST"):
    #         post_resource = "/store/order"
    #         json_for_create_order = {
    #         "id": id,
    #         "petId": petId,
    #         "quantity": quantity,
    #         "shipDate": shipDate,
    #         "status": status,
    #         "complete": complete
    #         }
    #         post_url = f"{base_url}{post_resource}"
    #         logger.add_request(post_url, method="POST",body=json_for_create_order)
    #         result_post = requests.post(post_url, json=json_for_create_order)
    #         logger.add_response(result_post.json())
    #         return result_post

    # """Find purchase order by ID"""
    # @staticmethod
    # def get_info_about_placed_order(order_id):
    #     with allure.step("GET"):
    #         get_resource="/store/order/"
    #         get_url=f"{base_url}{get_resource}{order_id}"
    #         logger.add_request(get_url, method="GET")
    #         result_get=requests.get(get_url)
    #         logger.add_response(result_get)
    #         print(result_get.text)
    #         return result_get

    #
    # """Delete purchase order by ID"""
    # @staticmethod
    # def delete_placed_order(order_id):
    #     with allure.step("DELETE"):
    #         delete_resource="/store/order/"
    #         delete_url=f"{base_url}{delete_resource}{order_id}"
    #         logger.add_request(delete_url, method="DELETE")
    #         result_delete=requests.delete(delete_url)
    #         logger.add_response(result_delete)
    #         print(result_delete.text)
    #         return result_delete
