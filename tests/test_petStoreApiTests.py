import json

import pytest
import requests

from api import ApiClient,StoreApi
from logger import Logger
from utils.checking_methods import Checking

import allure
from allure_commons.types import Severity
"""Test store api"""

logger=Logger()
client=ApiClient(logger)
store_api=StoreApi(client)

def test_create_first_order():
    create_first_order=store_api.place_order()
    print(create_first_order.status_code,create_first_order.json())
    Checking.check_status_code(response=create_first_order,status_code=200)
    Checking.check_json_value(response= create_first_order,field_name="status", expected_value="placed")
    Checking.check_json_answer(response=create_first_order,expected_value=["id", "petId", "quantity", "shipDate", "status", "complete"])


# @allure.epic('Epic Name')
# @allure.severity(Severity.CRITICAL)
# def test_example():
#     assert 1 == 1
# @allure.epic('Tests related access to Petstore orders')
# class TestStoreApi():
#
#     @allure.description('first test: post_order_and_get_info')
#     @pytest.mark.run(order=1)
#     def test_post_order_and_get_info(self):
#
#         """Returns pet inventories by status"""
#         print("GET /store/inventory")
#         result_get = Store.get_info_about_store()
#         Checking.check_status_code(result_get,200)
#         get_data = result_get.json()
#         print(json.dumps(get_data, indent=2))
#         get_data=json.loads(result_get.text)
#         print(list(get_data))
#         # Checking.check_json_answer(result_get,['sold', 'new', 'placed', 'string', 'alive', 'pending', 'available', 'inprogress', 'peric'])
#         print()
#         print()
#
#
#         """Place an order for a pet"""
#         print("POST /store/order")
#         result_post = Store.place_first_order()
#         post_data = result_post.json()
#         order_result = post_data["complete"]
#         order_id = post_data["id"]
#         assert order_result == True
#         Checking.check_status_code(result_post, 200)
#         print(json.dumps(post_data, indent=2))
#         # get_posted_data=json.loads(result_post.text)
#         # print(list(get_posted_data))
#         Checking.check_json_answer(result_post,['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'])
#         Checking.check_json_value(result_post,"status","placed")
#         print()
#         print()
#
#
#
#         """"Find purchase order by ID"""
#         print("GET /store/order/{orderId}")
#         result_get_posted_order=Store.get_info_about_placed_order(order_id)#alternative another method
#         # assert result_get_posted_order.status_code==200,"Problem with status_code GET_order request"
#         Checking.check_status_code(result_get_posted_order,200)
#         try:
#             get_data = result_get_posted_order.json()
#         except ValueError:
#             raise RuntimeError("JSON is not valid JSON")
#         print(json.dumps(get_data, indent=2))
#         # get_posted_data=json.loads(result_get_posted_order.text)
#         # print(list(get_posted_data))
#         Checking.check_json_answer(result_get_posted_order,['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'])
#         Checking.check_json_value(result_post, "complete", True)
#         print()
#         print()
#
#     @allure.description('second test: post_order_and_get_info')
#     @pytest.mark.run(order=2)
#     def test_post_get_delete_order(self):
#
#         """Place an order for a pet"""
#         print("POST /store/order")
#         result_post = Store.place_first_order()
#         # Checking.check_status_code(result_post, 200)
#         post_data = result_post.json()
#         order_result = post_data["complete"]
#         order_id = post_data["id"]
#         # assert order_result == True
#         print(json.dumps(post_data, indent=2))
#         # get_posted_data=json.loads(result_post.text)
#         # print(list(get_posted_data))
#         Checking.check_json_answer(result_post, ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'])
#         Checking.check_json_value(result_post, "quantity", 1)
#         Checking.check_json_search_word_in_value(result_post,"shipDate","2025")
#         print()
#         print()
#
#         """Find purchase order by ID"""
#         print("GET /store/order/{orderId}")
#         result_get_post= Store.get_info_about_placed_order(order_id)  # alternative another method
#         # assert result_get_post.status_code==200,"Problem with status_code GET_order request"
#         Checking.check_status_code(result_get_post, 200)
#         try:
#             get_data = result_get_post.json()
#         except ValueError:
#             raise RuntimeError("JSON is not valid JSON")
#         print(json.dumps(get_data, indent=2))
#         # get_posted_data=json.loads(result_get_post.text)
#         # print(list(get_posted_data))
#         Checking.check_json_answer(result_get_post,
#                                    ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'])
#         print()
#         print()
#         print()
#
#         print("DELETE /store/order/{orderId}")
#         result_delete_posted_order=Store.delete_placed_order(order_id)
#         # assert result_delete_posted_order.status_code==200,"Problem with status_code DELETE_order request"
#         Checking.check_status_code(result_delete_posted_order,200)
#         Checking.check_json_value(result_delete_posted_order,"code",200)

