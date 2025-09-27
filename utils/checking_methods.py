"""METHODS for checking responses of our requests"""
import json
import requests
import pytest
from typing import List, Tuple, Any


class Checking():

    @staticmethod
    @staticmethod
    def check_status_code(response, status_code):
        if not isinstance(response, requests.Response):
            raise TypeError(
                f"check_status_code очікує requests.Response, але отримав {type(response).__name__}"
            )

        if isinstance(status_code, (list, tuple, dict)):
            assert response.status_code in status_code, \
                f"Expected status codes: {status_code}, but got: {response.status_code}"
        else:
            assert response.status_code == status_code, \
                f"Expected status code: {status_code}, but got: {response.status_code}"






    @staticmethod
    def check_json_answer(response, expected_value):
        """
        Перевірка, що JSON-відповідь містить потрібні ключі.
        Працює як із requests.Response, так і з dict.
        """
        if isinstance(response, requests.Response):
            check = response.json()
        elif isinstance(response, dict):
            check = response
        else:
            raise TypeError(
                f"check_json_answer підтримує лише Response або dict, але отримав {type(response).__name__}"
            )

        if not check:
            raise AssertionError("Response JSON is empty")

        if isinstance(check, dict):
            for field in expected_value:
                assert field in check, \
                    f"Field '{field}' is missing in response JSON"
        elif isinstance(check, list):
            for item in check:
                for field in expected_value:
                    assert field in item, \
                        f"Field '{field}' is missing in response list item"
        else:
            raise TypeError(f"Unsupported JSON type: {type(check).__name__}")

    # def check_json_answer(response: requests.Response, expected_value):
    #     json_answer = response.json()
    #
    #     if not json_answer:
    #         raise AssertionError("Response JSON is empty.")
    #
    #     if isinstance(json_answer, list):
    #         data_to_check = json_answer[0]
    #     elif isinstance(json_answer, dict):
    #         data_to_check = json_answer
    #     else:
    #         raise TypeError(
    #             f"unexpected response format from the server. Check the response format : {type(json_answer)}")
    #
    #     actual_keys = set(data_to_check.keys())
    #     expected_keys = set(expected_value)
    #
    #     # Check if all expected keys are present in actual keys
    #     missing_keys = expected_keys - actual_keys
    #     if missing_keys:
    #         raise AssertionError(f"Expected keys {missing_keys} are missing. Actual keys: {actual_keys}")










    @staticmethod
    def check_json_value(response: requests.Response, field_name: str, expected_value: Any):
        # check = response.json()

        if isinstance(response, requests.Response):
            check = response.json()
        elif isinstance(response, dict):
            check = response
        else:
            raise TypeError(
                f"check_json_value підтримує лише Response або dict, але отримав {type(response).__name__}"
            )

        if not check:
            raise AssertionError("Response JSON is empty")

        if isinstance(check, list):
            """If it is a list, you need to check each element."""
            for item in check:
                assert item.get(field_name) == expected_value, \
                    f"Value for field '{field_name}' in list mismatch. Expected: '{expected_value}', but got: '{item.get(field_name)}'"
        elif isinstance(check, dict):
            """If it's a dictionary, you need to check it directly."""
            assert check.get(field_name) == expected_value, \
                f"Value for field '{field_name}' in dict mismatch. Expected: '{expected_value}', but got: '{check.get(field_name)}'"
        else:
            raise TypeError(f"Unsupported JSON type: {type(check).__name__}")





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
