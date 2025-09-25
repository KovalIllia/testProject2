"""METHODS for checking responses of our requests"""
import json
import requests
import pytest

class Checking():

    @staticmethod
    def check_status_code(response: requests.Response, status_code):
        """
        Checks the response status code. Can handle a single integer or a list/tuple of integers.
        """
        if isinstance(status_code, (list, tuple)):
            assert response.status_code in status_code, \
                f"Expected status codes: {status_code}, but got: {response.status_code}"
        else:
            assert response.status_code == status_code, \
                f"Expected status code: {status_code}, but got: {response.status_code}"


    @staticmethod
    def check_json_answer(response: requests.Response, expected_fields):
        json_answer = response.json()

        if not json_answer:
            raise AssertionError("Response JSON is empty.")


        if isinstance(json_answer, list):
            data_to_check = json_answer[0]
        elif isinstance(json_answer, dict):
            data_to_check = json_answer
        else:
            raise TypeError(f"unexpected response format from the server. Check the response format : {type(json_answer)}")

        actual_keys = list(data_to_check.keys())

        for field in expected_fields:
            assert field in actual_keys, f"Ecspected response: '{field}', but actual result is different: '{actual_keys}'"




    @staticmethod
    def check_json_value(response: requests.Response, field_name, expected_value):
        check = response.json()

        if not check:
            raise AssertionError("Response JSON is empty")

        if isinstance(check, list):
            """If it is a list, you need to check each element."""
            for pet in check:
                assert pet.get(field_name) == expected_value, \
                    f"Value for field '{field_name}' in list mismatch. Expected: '{expected_value}', but got: '{pet.get(field_name)}'"
        elif isinstance(check, dict):
            """If it's a dictionary, you need to check it directly."""
            assert check.get(field_name) == expected_value, \
                f"Value for field '{field_name}' in dict mismatch. Expected: '{expected_value}', but got: '{check.get(field_name)}'"
        else:
            raise TypeError(f"Unsupported JSON type: {type(check)}")





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
