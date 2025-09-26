import time

class PetWaiter:
    @staticmethod
    def wait_for_pet(pet_api, pet_id: int, expected_status=200, retries=10, delay=1):

        for _ in range(retries):
            response = pet_api.find_pet_by_id(pet_id)
            if response.status_code == expected_status:
                return response
            time.sleep(delay)
        raise AssertionError(
            f"Pet {pet_id} did not return status {expected_status} after {retries} retries"
        )