import time

import pytest
import allure
from allure_commons.types import Severity

from utils.checking_methods import Checking


import allure
from allure_commons.types import Severity



def test_get_inventories_by_status(store_api):
    get_inventories=store_api.get_inventory()
    print(get_inventories.status_code,get_inventories.json())
    Checking.check_status_code(response=get_inventories,status_code=200)


def test_create_first_order(place_order_for_a_pet):
    print("Created order:", place_order_for_a_pet.json())
    print(place_order_for_a_pet.status_code,place_order_for_a_pet.json())
    Checking.check_status_code(response=place_order_for_a_pet,status_code=200)
    Checking.check_json_value(response= place_order_for_a_pet,field_name="status", expected_value="placed")
    Checking.check_json_answer(response=place_order_for_a_pet,expected_value=["id", "petId", "quantity", "shipDate", "status", "complete"])


def wait_for_order(order_id, store_api,retries=3, delay=1):
    for attempt in range(1, retries + 1):
        response = store_api.get_info_about_placed_order_by_id(order_id)
        if response.status_code == 200:
            return response
        print(f"[Retry {attempt}] Order {order_id} not found, got {response.status_code}")
        time.sleep(delay)
    raise AssertionError(f"Order {order_id} not found after {retries} attemps")

@pytest.mark.skip(reason="Swagger Petstore demo API does not persist orders")
def test_find_purchase_order_by_id(place_order_for_a_pet,store_api):
    order_id=place_order_for_a_pet.json()["id"]
    find_purchase_order_by_id=wait_for_order(order_id,store_api)
    print(find_purchase_order_by_id.status_code,find_purchase_order_by_id.json())
    Checking.check_status_code(response=find_purchase_order_by_id, status_code=[200,404])
    Checking.check_json_value(response=find_purchase_order_by_id, field_name="status", expected_value="placed")
    Checking.check_json_answer(response=find_purchase_order_by_id,expected_value=["id", "petId", "quantity", "shipDate", "status", "complete"])


@pytest.mark.skip(reason="Swagger Petstore demo API does not persist orders")
def test_delete_purchase_order_by_id(place_order_for_a_pet,store_api):
    order_id=place_order_for_a_pet.json()["id"]
    delete_purchase_order_by_id=store_api.delete_placed_order(order_id)
    print(delete_purchase_order_by_id.status_code,delete_purchase_order_by_id.json())
    Checking.check_status_code(response=delete_purchase_order_by_id,status_code=200)

