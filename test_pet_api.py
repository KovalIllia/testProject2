from utils.checking_methods import Checking

"""Initialize the clients"""


# logger=Logger()
# client=ApiClient(logger)
# pet_api_client=PetApi(client)


# @pytest.fixture(scope="session")
# def create_pet(pet_api):
#     pet_body=PetFactory.default_pet(status="available")
#     response=pet_api_client.add_pet(pet_body)
#     return response

def test_add_pet(create_pet, pet_api):
    print(create_pet.status_code, create_pet.json())
    Checking.check_status_code(response=create_pet, status_code=200)
    Checking.check_json_value(response=create_pet, field_name="status", expected_value="available")
    Checking.check_json_answer(response=create_pet,
                               expected_value=["id", "category", "name", "photoUrls", "tags", "status"])


def test_update_pet(create_pet, pet_api):
    print(create_pet.status_code, create_pet.json())
    Checking.check_status_code(response=create_pet, status_code=200)
    Checking.check_json_value(response=create_pet, field_name="status", expected_value="available")
    Checking.check_json_answer(response=create_pet,
                               expected_value=["id", "category", "name", "photoUrls", "tags", "status"])


def test_find_pet_by_status(pet_api,):
    get_available_pet=pet_api.find_pet_by_status()
    print(get_available_pet.status_code,get_available_pet.json())