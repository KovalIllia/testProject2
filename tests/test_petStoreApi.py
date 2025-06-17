import json

from utils.api import Store

# import allure

"""Test store api"""


class TestStoreApi():

    def test_get_info(self):
        print("GET /store/inventory")
        result_get = Store.get_info_about_store()
        assert result_get.status_code == 200
        get_data = result_get.json()
        print(json.dumps(get_data, indent=2))

    def test_post_order(self):
        print("POST /store/order")
        result_post = Store.place_order()
        assert result_post.status_code == 200, f"Wrong status code"
        try:
            post_data = result_post.json()
        except ValueError:
            raise RuntimeError("JSON is not valid JSON")
        order_result = post_data["complete"]
        assert order_result == True
        print(json.dumps(post_data, indent=2))
