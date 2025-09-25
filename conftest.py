import pytest

from api.base_api import ApiClient
from api.files_api import FilesApi
from api.store_api import StoreApi
from api.pet_api import PetApi
from tests.factories.order_factory import OrderFactory
from tests.factories.pet_factory import PetFactory
from utils.logger import Logger


@pytest.fixture(scope="session")
def api_client():
    logger = Logger()
    return ApiClient(logger)

@pytest.fixture(scope="session")
def store_api(api_client):
    return StoreApi(api_client)

@pytest.fixture(scope="session")
def pet_api(api_client):
    return PetApi(api_client)

@pytest.fixture(scope="session")
def place_order_for_a_pet(store_api):
    order_body = OrderFactory.default_order(quantity=3)
    response = store_api.place_order(order_body)
    return response

@pytest.fixture(scope="function")
def pet_payload(pet_api):
    return PetFactory.default_pet(name="Rex", status="available")


@pytest.fixture(scope="session")
def files_client(logger):
    return FilesApi(base_url="https://petstore.swagger.io/v2", logger=logger)

@pytest.fixture(scope="session")
def logger():
    return Logger