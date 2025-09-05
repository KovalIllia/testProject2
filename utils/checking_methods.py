"""METHODS for checking responses of our requests"""
import json
import requests
import pytest

class Checking():


    """method for checking status code"""
    @staticmethod
    def check_status_code(response: requests.Response, status_code:int):
        assert response.status_code == status_code# espectedResult==actualResult
        if response.status_code==status_code:
            print(f"success! status code: {response.status_code}")
        else:
            print(f"failed!error! status code: {response.status_code}")




    """method for checking for required FIELDS in a query response"""
    @staticmethod
    def check_json_answer(response: requests.Response, expected_value):
        json_answer=json.loads(response.text)
        assert list(json_answer)==expected_value
        print("all required field are presented")


    """method for checking for required fields VALUES in a query response"""
    @staticmethod
    def check_json_value(response: requests.Response, field_name, expected_value):
        check=response.json()
        check_info=check[field_name]
        assert check_info==expected_value
        print(f"{field_name} --- is correct")


    """method for checking for required fields Values in a query response with required key"""
    @staticmethod
    def check_json_search_word_in_value(response: requests.Response,field_name,search_word):
        check=response.json()
        check_info=check[field_name]
        if search_word in check_info:
            print(f"search word {field_name} == is correct")
        else:
            print("operation failed")