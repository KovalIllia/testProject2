# import json
# from datetime import time
#
# import pytest
# import requests
#
# from api import ApiClient, store_api, pet_api
# from factories.order_factory import OrderFactory
# from factories.pet_factory import PetFactory
# from logger import Logger
# from utils.checking_methods import Checking
#
# import allure
# from allure_commons.types import Severity
# """Test store api"""
#
# logger=Logger()
# client=ApiClient(logger)
# store_api=StoreApi(client)
# pet_api=PetApi(client)
#
# @pytest.fixture(scope="session")
# def place_order_for_a_pet():
#     order_body=OrderFactory.default_order(quantity=3)
#     response=store_api.place_order(order_body)
#     return response
#
# @pytest.fixture(scope="session")
# def create_pet():
#     pet_body=PetFactory.default_pet(name="Rex",status="available")
#     response=pet_api.add_pet(pet_body)
#     return response
#
#
#
# def test_get_inventories_by_status():
#     get_inventories=store_api.get_inventory()
#     print(get_inventories.status_code,get_inventories.json())
#     Checking.check_status_code(response=get_inventories,status_code=200)
#
# # @allure.epic('Tests related access to Petstore orders')
# # @allure.severity(Severity.CRITICAL)
# def test_create_first_order(place_order_for_a_pet):
#     print(place_order_for_a_pet.status_code,place_order_for_a_pet.json())
#     Checking.check_status_code(response=place_order_for_a_pet,status_code=200)
#     Checking.check_json_value(response= place_order_for_a_pet,field_name="status", expected_value="placed")
#     Checking.check_json_answer(response=place_order_for_a_pet,expected_value=["id", "petId", "quantity", "shipDate", "status", "complete"])
#
#
# def wait_for_order(order_id, retries=3, delay=1):
#     for _ in range(retries):
#         response = store_api.get_info_about_placed_order_by_id(order_id)
#         if response.status_code == 200:
#             return response
#         time.sleep(delay)
#     return response
#
#
# def test_find_purchase_order_by_id(place_order_for_a_pet):
#     order_id=place_order_for_a_pet.json()["id"]
#     find_purchase_order_by_id=store_api.get_info_about_placed_order_by_id(order_id)
#     print(find_purchase_order_by_id.status_code,find_purchase_order_by_id.json())
#     Checking.check_status_code(response=find_purchase_order_by_id, status_code=200)
#     Checking.check_json_value(response=find_purchase_order_by_id, field_name="status", expected_value="placed")
#     Checking.check_json_answer(response=find_purchase_order_by_id,expected_value=["id", "petId", "quantity", "shipDate", "status", "complete"])
#
# def test_delete_purchase_order_by_id(place_order_for_a_pet):
#     order_id=place_order_for_a_pet.json()["id"]
#     delete_purchase_order_by_id=store_api.delete_placed_order(order_id)
#     print(delete_purchase_order_by_id.status_code,delete_purchase_order_by_id.json())
#     Checking.check_status_code(response=delete_purchase_order_by_id,status_code=200)
#     # Checking.check_status_code(response=delete_purchase_order_by_id,status_code=200)
#
#
#
# def test_add_pet(create_pet):
#     print(create_pet.status_code, create_pet.json())
#     Checking.check_status_code(response=create_pet, status_code=200)
#     Checking.check_json_value(response=create_pet, field_name="status", expected_value="available")
#     Checking.check_json_value(response=create_pet,expected_value=["id", "category", "name", "photoUrls", "tags", "status"])