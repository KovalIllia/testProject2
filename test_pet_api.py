import pytest
import allure
from allure_commons.types import Severity


from api.base_api import ApiClient
from api.pet_api import PetApi
from factories.pet_factory import PetFactory
from utils.logger import Logger
from utils.checking_methods import Checking

import allure
from allure_commons.types import Severity


"""Initialize the clients"""
# logger=Logger()
# client=ApiClient(logger)
# pet_api_client=PetApi(client)


# @pytest.fixture(scope="session")
# def create_pet(pet_api):
#     pet_body=PetFactory.default_pet(status="available")
#     response=pet_api_client.add_pet(pet_body)
#     return response

def test_add_pet(create_pet,pet_api):
    print(create_pet.status_code, create_pet.json())
    Checking.check_status_code(response=create_pet, status_code=200)
    Checking.check_json_value(response=create_pet, field_name="status", expected_value="available")
    Checking.check_json_answer(response=create_pet,expected_value=["id", "category", "name", "photoUrls", "tags", "status"])