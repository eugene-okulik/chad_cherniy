import os

import allure
import requests
from dotenv import load_dotenv


load_dotenv()


class BaseEndpoint:
    url = os.getenv("MAIN_URL")

    def __init__(self):
        self.response = None
        self.json = None

    def _request(self, method, path, payload=None, headers=None):
        self.response = requests.request(
            method=method,
            url=f"{self.url}{path}",
            timeout=20,
            json=payload,
            headers=headers,
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return self.response

    @allure.step("Check status code is {expected_status}")
    def check_status_code(self, expected_status):
        actual_status = self.response.status_code if self.response is not None else None
        if isinstance(expected_status, (list, tuple, set)):
            assert actual_status in expected_status, (
                f"Expected status code in {expected_status}, got {actual_status}"
            )
            return
        assert actual_status == expected_status, (
            f"Expected status code {expected_status}, got {actual_status}"
        )

    @allure.step("Check field '{field_name}'")
    def check_field_value(self, field_name, expected_value):
        actual_value = self.json[field_name]
        assert actual_value == expected_value, (
            f"Expected '{field_name}' to be {expected_value}, got {actual_value}"
        )

    @allure.step("Check object id is {expected_id}")
    def check_object_id(self, expected_id):
        actual_id = int(self.json["id"])
        assert actual_id == expected_id, (
            f"Expected object id {expected_id}, got {actual_id}"
        )
