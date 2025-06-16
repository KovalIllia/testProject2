import json

import requests


base_url = "https://petstore.swagger.io/v2"


class Store():
    """Access to Petstore orders"""

    """Returns pet inventories by status"""
    @staticmethod
    def get_info_about_store():
        get_resource ="/store/inventory"
        get_url=f"{base_url}{get_resource}"
        result_get=requests.get(get_url)
        return result_get





