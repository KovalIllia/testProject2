import json
import  requests
import pytest
from utils.checking_methods import Checking
from config.api import Store

# import allure

"""Test store api"""

@pytest.fixture(scope="function")
def test_post_order():
    print("POST /store/order")
    result_post = Store.place_FirstOrder()
    # assert result_post.status_code == 200, f"Wrong status code"
    post_data = result_post.json()
    order_result = post_data["complete"]
    order_id = post_data["id"]
    # assert order_result == True
    print(json.dumps(post_data, indent=2))
    Checking.check_status_code(result_post,200)
    return order_id
    yield order_id
    Store.delete_placed_order(order_id)


class TestStoreApi():

    def test_get_info(self):
        print("GET /store/inventory")
        result_get = Store.get_info_about_store()
        assert result_get.status_code==200
        get_data = result_get.json()
        print(json.dumps(get_data, indent=2))
        # get_data=json.loads(result_get.text)
        # print(list(get_data))
        Checking.check_json_answer(result_get,['sold', 'asd', 'string', 'unavailable', 'pending', 'available', 'Not Available', 'Available', 'peric'])

    # def test_post_order(self):
    #     print("POST /store/order")
    #     result_post = Store.place_order()
    #     assert result_post.status_code == 200, f"Wrong status code"
    #     try:
    #         post_data = result_post.json()
    #     except ValueError:
    #         raise RuntimeError("JSON is not valid JSON")
    #     order_result = post_data["complete"]
    #     order_id=post_data["id"]
    #     assert order_result == True
    #     print(json.dumps(post_data, indent=2))

    def test_get_placed_order(self,post_order):
        print("GET /store/order/{orderId}")
        result_get_posted_order: requests.Response=Store.get_info_about_placed_order(post_order)#alternative another method
        # assert result_get_posted_order.status_code==200,"Problem with status_code GET_order request"
        Checking.check_status_code(result_get_posted_order,200)
        try:
            get_data = result_get_posted_order.json()
        except ValueError:
            raise RuntimeError("JSON is not valid JSON")
        print(json.dumps(get_data, indent=2))


    # def test_delete_placed_order(self,post_order):
    #     print("DELETE /store/order/{orderId}")
    #     result_delete_posted_order:requests.Response=Store.delete_placed_order(post_order)
    #     # assert result_delete_posted_order.status_code==200,"Problem with status_code DELETE_order request"
    #     Checking.check_status_code(result_delete_posted_order,200)