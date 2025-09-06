import pytest

from api import pet_api
from factories.order_factory import OrderFactory

from api.base_api import ApiClient
from api.store_api import StoreApi
from factories.pet_factory import PetFactory
from utils.logger import Logger
from utils.checking_methods import Checking
from factories.order_factory import OrderFactory

"""Initialize the clients"""
logger=Logger()
client=ApiClient(logger)
store_api=StoreApi(client)

@pytest.fixture(scope="session")
def place_order_for_a_pet():
    order_body=OrderFactory.default_order(quantity=3)
    response=store_api.place_order(order_body)
    return response

@pytest.fixture(scope="session")
def create_pet():
    pet_body=PetFactory.default_pet(name="Rex",status="available")
    response=pet_api.add_pet(pet_body)
    return response

@pytest.fixture(scope="session")
def api_client():
    logger = Logger()
    return ApiClient(logger)

@pytest.fixture(scope="session")
def store_api(api_client):
    return StoreApi(api_client)