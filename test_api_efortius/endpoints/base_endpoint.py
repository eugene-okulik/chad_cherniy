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
