import time

from tests.factories.file_factory import FileFactory
from tests.factories.pet_factory import UpdatePetFactory
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


def test_find_pet_by_status(pet_api):
    get_available_pet=pet_api.find_pet_by_status()
    print(get_available_pet.status_code,get_available_pet.json())



def test_find_pet_by_id (create_pet,pet_api):
    created_pet=create_pet.json()["id"]
    looking_pet_by_id=pet_api.find_pet_by_id(created_pet)
    Checking.check_status_code(response=create_pet, status_code=200)
    Checking.check_json_value(response=create_pet, field_name="status", expected_value="available")
    Checking.check_json_answer(response=create_pet,
                               expected_value=["id", "category", "name", "photoUrls", "tags", "status"])




def wait_for_pet(pet_id, pet_api, retries=3, delay=1):
    for attempt in range(1, retries + 1):
        response = pet_api.find_pet_by_id(pet_id)
        if response.status_code == 200:
            return response
        print(f"[Retry {attempt}] Pet {pet_id} not available, status {response.status_code}")
        time.sleep(delay)
    raise AssertionError(f"Pet {pet_id} not found after {retries} attemps")



def test_update_pet_with_form(create_pet,pet_api):
    created_pet=create_pet.json()["id"]
    wait_for_pet(created_pet,pet_api,retries=5,delay=1)
    update_pet=UpdatePetFactory.update_pet_with_name_and_status("Lopik","sold")
    response_with_update=pet_api.update_pet_with_form_data(created_pet,update_pet)
    print(response_with_update.status_code,response_with_update.text)
    Checking.check_status_code(response=response_with_update, status_code=200)
    Checking.check_json_value(response=response_with_update, field_name="message", expected_value=str(created_pet))


def wait_for_pet(pet_id, pet_api, retries=3, delay=1):
    for attempt in range(1, retries + 1):
        response = pet_api.find_pet_by_id(pet_id)
        if response.status_code == 200:
            return response
        print(f"[Retry {attempt}] Pet {pet_id} not available, status {response.status_code}")
        time.sleep(delay)
    raise AssertionError(f"Pet {pet_id} not found after {retries} attemps")


def test_delete_pet(create_pet,pet_api):
    created_pet=create_pet.json()["id"]
    delete_pet_by_id=pet_api.delete_pet(created_pet)
    print(delete_pet_by_id.status_code,delete_pet_by_id.json())
    Checking.check_status_code(response=delete_pet_by_id, status_code=200)

def test_upload_pet_image(create_pet,files_client):
    created_pet=create_pet.json()["id"]
    files_path=FileFactory.pet_image("dog.png")

    upload_result=files_client.upload_pet_image(created_pet,files_path,"smiled_dog")

    print(upload_result.status_code,upload_result.json())
    Checking.check_status_code(response=upload_result,status_code=200)
    # Checking.check_message_contains(response=upload_result,expected_substring="smiled_dog")