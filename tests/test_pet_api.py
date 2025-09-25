import time

from conftest import pet_payload
from tests.factories.file_factory import FileFactory
from tests.factories.pet_factory import UpdatePetFactory
from utils.checking_methods import Checking
from utils.enums import PetStatus



def test_add_pet(pet_api, pet_payload):

    creating_pet=pet_api.add_pet(pet_payload)

    Checking.check_status_code(response=creating_pet, status_code=200)
    Checking.check_json_value(response=creating_pet, field_name="status", expected_value="available")
    Checking.check_json_answer(response=creating_pet,
                               expected_value=["id", "category", "name", "photoUrls", "tags", "status"])



def test_update_pet(pet_api,pet_payload):

    creating_pet_response = pet_api.add_pet(pet_payload)
    original_pet_data=dict(creating_pet_response.json())

    update_fields=UpdatePetFactory.update_pet_with_name_and_status(name="Alfred",
                                                                   status="sold")

    copied_pet_data=original_pet_data.copy()
    copied_pet_data.update(update_fields)
    updated_pet=pet_api.update_pet(copied_pet_data)

    Checking.check_status_code(response=updated_pet, status_code=200)
    Checking.check_json_value(response=updated_pet, field_name="status", expected_value="sold")
    Checking.check_json_value(response=updated_pet,field_name="name",expected_value="Alfred")
    Checking.check_json_answer(response=updated_pet,
                               expected_value=["id", "category", "name", "photoUrls", "tags", "status"])




def test_get_pets_by_status(pet_api, pet_payload):

    find_pet_by_response=pet_api.find_pet_by_status(status=PetStatus.AVAILABLE)

    Checking.check_status_code(response=find_pet_by_response, status_code=200)
    Checking.check_json_value(response=find_pet_by_response, field_name="status", expected_value="available")
    Checking.check_json_answer(response=find_pet_by_response,
                               expected_value=["id", "category", "name", "photoUrls", "tags", "status"])




def test_find_pet_by_id (pet_api, pet_payload):
    creating_pet = pet_api.add_pet(pet_payload)

    created_pet=creating_pet.json()
    pet_id=created_pet["id"]
    looking_pet_by_id=pet_api.find_pet_by_id(pet_id)


    Checking.check_status_code(response=looking_pet_by_id, status_code=200)
    Checking.check_json_value(response=looking_pet_by_id, field_name="status", expected_value="available")
    Checking.check_json_answer(response=looking_pet_by_id,
                               expected_value=["id", "category", "name", "photoUrls", "tags", "status"])
















def test_update_pet_with_form(pet_api,pet_payload):

    creating_pet = pet_api.add_pet(pet_payload)
    created_pet = creating_pet.json()
    pet_id = created_pet["id"]

    # wait_for_pet(pet_id,pet_api,retries=10,delay=1)

    found_pet = wait_for_pet(pet_id, pet_api, retries=10, delay=1)
    Checking.check_status_code(found_pet, 200)

    response_with_update = pet_api.update_pet_with_form_data(
        pet_id,
        name="Lopik",
        status="sold"
    )

    updated_pet = wait_for_pet(pet_id, pet_api, retries=10, delay=1)
    Checking.check_status_code(response=response_with_update, status_code=200)
    Checking.check_json_value(response=response_with_update, field_name="message", expected_value=str(pet_id))




def wait_for_pet(pet_id, pet_api, retries=10, delay=1):
    for i in range(retries):
        response = pet_api.find_pet_by_id(pet_id)
        if response.status_code == 200:
            return response
        # Якщо статус 404, ми чекаємо і робимо наступну спробу
        time.sleep(delay)
    # Якщо після всіх спроб ми так і не отримали 200, ми кидаємо помилку
    raise AssertionError(f"Pet with ID {pet_id} not found after {retries} retries.")

























def test_delete_pet(pet_payload, pet_api):
    created_pet=pet_payload.json()["id"]
    delete_pet_by_id=pet_api.delete_pet(created_pet)
    print(delete_pet_by_id.status_code,delete_pet_by_id.text)
    if delete_pet_by_id.content:
        print(delete_pet_by_id.json())
    Checking.check_status_code(response=delete_pet_by_id, status_code=[200,204,404])

def test_upload_pet_image(pet_payload, files_client):
    created_pet=pet_payload.json()["id"]
    files_path=FileFactory.pet_image("dog.png")

    upload_result=files_client.upload_pet_image(created_pet,files_path,"smiled_dog")

    print(upload_result.status_code,upload_result.json())
    Checking.check_status_code(response=upload_result,status_code=200)
