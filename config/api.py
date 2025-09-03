
import requests
from utils.logger import Logger
import allure
from collections.abc import Mapping


base_url = "https://petstore.swagger.io/v2"
logger = Logger()

class Store():
    """Access to Petstore orders"""

    """Returns pet inventories by status"""

    @staticmethod
    def get_info_about_store():
        with allure.step("GET"):
            get_resource = "/store/inventory"
            get_url = f"{base_url}{get_resource}"
            logger.add_request(get_url, method="GET")
            result_get = requests.get(get_url)
            Logger.add_request(result_get, method="GET")
            Logger.add_response(result_get)
            return result_get



    """Place an order for a pet #1"""
    @staticmethod
    def place_first_order():
        with allure.step("POST"):
            post_resource = "/store/order"
            json_for_creat_order = {
            "id": 1,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2025-06-17T19:25:58.960Z",
            "status": "placed",
            "complete": True
            }
            post_url = f"{base_url}{post_resource}"
            logger.add_request(post_url, method="POST")
            result_post=requests.post(post_url,json=json_for_creat_order)
            logger.add_response(result_post)
            return result_post

    """Place an order for a pet #2"""

    @staticmethod
    def place_second_order():
        with allure.step("POST"):
            post_resource = "/store/order"
            json_for_creat_order = {
            "id": 22,
            "petId": 22,
            "quantity": 1,
            "shipDate": "2025-06-17T19:25:58.960Z",
            "status": "placed",
            "complete": True
            }
            post_url = f"{base_url}{post_resource}"
            logger.add_request(post_url, method="POST")
            result_post = requests.post(post_url, json=json_for_creat_order)
            logger.add_response(result_post)
            return result_post

    """Find purchase order by ID"""
    @staticmethod
    def get_info_about_placed_order(order_id):
        with allure.step("GET"):
            get_resource="/store/order/"
            get_url=f"{base_url}{get_resource}{order_id}"
            logger.add_request(get_url, method="GET")
            result_get=requests.get(get_url)
            logger.add_response(result_get)
            print(result_get.text)
            return result_get


    """Delete purchase order by ID"""
    @staticmethod
    def delete_placed_order(order_id):
        with allure.step("DELETE"):
            delete_resource="/store/order/"
            delete_url=f"{base_url}{delete_resource}{order_id}"
            logger.add_request(delete_url, method="DELETE")
            result_delete=requests.delete(delete_url)
            logger.add_response(result_delete)
            print(result_delete.text)
            return result_delete
