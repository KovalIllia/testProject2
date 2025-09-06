import time

import pytest
import allure
from allure_commons.types import Severity

from api.base_api import ApiClient
from api.store_api import StoreApi
from utils.logger import Logger
from utils.checking_methods import Checking
from factories.order_factory import OrderFactory

import allure
from allure_commons.types import Severity


"""Initialize the clients"""
# conftest.py# conftest.py
# logger=Logger()
# client=ApiClient(logger)
# store_api=StoreApi(client)


def test_get_inventories_by_status():
    get_inventories=store_api.get_inventory()
    print(get_inventories.status_code,get_inventories.json())
    Checking.check_status_code(response=get_inventories,status_code=200)

# @allure.epic('Tests related access to Petstore orders')
# @allure.severity(Severity.CRITICAL)
def test_create_first_order(place_order_for_a_pet):
    print(place_order_for_a_pet.status_code,place_order_for_a_pet.json())
    Checking.check_status_code(response=place_order_for_a_pet,status_code=200)
    Checking.check_json_value(response= place_order_for_a_pet,field_name="status", expected_value="placed")
    Checking.check_json_answer(response=place_order_for_a_pet,expected_value=["id", "petId", "quantity", "shipDate", "status", "complete"])


def wait_for_order(order_id, retries=3, delay=1):
    for _ in range(retries):
        response = store_api.get_info_about_placed_order_by_id(order_id)
        if response.status_code == 200:
            return response
        time.sleep(delay)
    return response


def test_find_purchase_order_by_id(place_order_for_a_pet):
    order_id=place_order_for_a_pet.json()["id"]
    find_purchase_order_by_id=store_api.get_info_about_placed_order_by_id(order_id)
    print(find_purchase_order_by_id.status_code,find_purchase_order_by_id.json())
    Checking.check_status_code(response=find_purchase_order_by_id, status_code=200)
    Checking.check_json_value(response=find_purchase_order_by_id, field_name="status", expected_value="placed")
    Checking.check_json_answer(response=find_purchase_order_by_id,expected_value=["id", "petId", "quantity", "shipDate", "status", "complete"])

def test_delete_purchase_order_by_id(place_order_for_a_pet):
    order_id=place_order_for_a_pet.json()["id"]
    delete_purchase_order_by_id=store_api.delete_placed_order(order_id)
    print(delete_purchase_order_by_id.status_code,delete_purchase_order_by_id.json())
    Checking.check_status_code(response=delete_purchase_order_by_id,status_code=200)
    # Checking.check_status_code(response=delete_purchase_order_by_id,status_code=200)
