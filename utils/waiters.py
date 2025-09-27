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


class StoreWaiter:
    @staticmethod
    def wait_for_order(store_api, order_id: int, expected_status: int=200, retries:int=10, delay:int=1):
        for attempt in range(1, retries + 1):
            response = store_api.get_info_about_placed_order_by_id(order_id)
            if response.status_code == expected_status:
                return response
            print(f"[Retry {attempt}] Order {order_id} not found, got {response.status_code}")
            time.sleep(delay)

        raise AssertionError(f"Order {order_id} not found after {retries} attempts")
