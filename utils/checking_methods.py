"""METHODS for checking responses of our requests"""
import json
import requests
import pytest

class Checking():


    """method for checking status code"""

    @staticmethod
    def check_status_code(response: requests.Response, status_code):
        match status_code:
            case list() | tuple() | set():
                assert response.status_code in status_code,(f"Expected result: status code:{status_code}, "
                                                          f"but actual result: status code: {response.status_code}")
            case int():
                assert response.status_code == status_code,(f"Expected result: status code:{status_code}, "
                                                          f"but actual result: status code: {response.status_code}")
            case str() | None:
                raise TypeError(f"Unsupported type for status_code: status code:{type(status_code).__name__}, "
                                                          f"but actual result: status code: {response.status_code}")






    """method for checking for required FIELDS in a query response"""
    @staticmethod
    def check_json_answer(response: requests.Response, expected_fields):
        json_answer=json.loads(response.text)
        actual_keys_fields=list(json_answer.keys())
        assert set(actual_keys_fields)==set(expected_fields), f"Expected fields: {expected_fields}, but got: {actual_keys_fields}"



    """method for checking for required fields VALUES in a query response"""
    @staticmethod
    def check_json_value(response: requests.Response, field_name, expected_value):
        check=response.json()
        check_info=check.get(field_name)
        assert check_info==expected_value,f"Field '{field_name}' mismatch. Expected: {expected_value}, got: {check_info}"



    """method for checking for required fields Values/Keywords in a query response with required key"""
    @staticmethod
    def check_json_search_word_in_value(response: requests.Response,field_name,search_word):
        check=response.json()
        check_info=check[field_name]
        if not isinstance(check_info,str) :
            raise TypeError(f"Field '{field_name}' should be a string, got {type(check_info).__name__}")
        assert search_word in check_info,f"Keyword '{search_word}' missing in field '{field_name}', value: {check_info}"



    @staticmethod
    def check_message_contains(response:requests.Response,expected_substring:str):
        check=response.json()
        key_message=check.get("message", "")
        assert expected_substring in key_message,f"the {key_message} does not contain expected substring: {expected_substring}"
