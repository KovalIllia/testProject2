import pytest
import allure
from allure_commons.types import Severity


from api.base_api import ApiClient
from api.pet_api import PetApi
from factories.pet_factory import PetFactory
from utils.logger import Logger
from utils.checking_methods import Checking
from factories.order_factory import OrderFactory

import allure
from allure_commons.types import Severity


"""Initialize the clients"""
logger=Logger()
client=ApiClient(logger)
pet_api_client=PetApi(client)


@pytest.fixture(scope="session")
def create_pet():
    pet_body=PetFactory.default_pet(status="available")
    response=pet_api_client.add_pet(pet_body)
    return response