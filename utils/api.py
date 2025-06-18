import requests

base_url = "https://petstore.swagger.io/v2"


class Store():
    """Access to Petstore orders"""

    """Returns pet inventories by status"""

    @staticmethod
    def get_info_about_store():
        get_resource = "/store/inventory"
        get_url = f"{base_url}{get_resource}"
        result_get = requests.get(get_url)
        return result_get



    """Place an order for a pet"""
    @staticmethod
    def place_order():
        post_resource = "/store/order"
        json_for_creat_order = {
            "id": 1,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2025-06-17T19:25:58.960Z",
            "status": "placed",
            "complete": True
        }
        post_url = f"{base_url}{post_resource}"
        result_post=requests.post(post_url,json=json_for_creat_order)
        return result_post

    """Find purchase order by ID"""
    @staticmethod
    def get_info_about_placed_order(order_id):
        get_resource="/store/order/"
        get_url=f"{base_url}{get_resource}{order_id}"
        result_get=requests.get(get_url)
        return result_get


    """Delete purchase order by ID"""
    @staticmethod
    def delete_placed_order(order_id):
        delete_resource="/store/order/"
        delete_url=f"{base_url}{delete_resource}{order_id}"
        result_delete=requests.delete(delete_url)
        print(result_delete.text)
        return result_delete
