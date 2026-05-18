import logging
import os
import requests
import allure
from dotenv import load_dotenv


load_dotenv()
logger = logging.getLogger(__name__)


class BaseEndpoint:
    url = os.getenv("MEME_URL", "http://memesapi.course.qa-practice.com")

    def __init__(self):
        self.response = None
        self.json = None

    def _request(self, method, path, payload=None, token=None, headers=None):
        request_headers = headers.copy() if headers else {}
        if token:
            request_headers["Authorization"] = token

        logger.info("Sending %s request to %s", method, path)
        self.response = requests.request(
            method=method,
            url=f"{self.url}{path}",
            timeout=20,
            json=payload,
            headers=request_headers or None,
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        logger.info("Received status code %s", self.response.status_code)
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

    @allure.step("Check response has field {field_name}")
    def check_field_exists(self, field_name):
        assert self.json is not None, "Response body is not JSON"
        assert field_name in self.json, f"Field '{field_name}' is absent in response"

    @allure.step("Check field {field_name} value")
    def check_field_value(self, field_name, expected_value):
        self.check_field_exists(field_name)
        actual_value = self.json[field_name]
        assert actual_value == expected_value, (
            f"Expected '{field_name}' to be {expected_value}, got {actual_value}"
        )

    @allure.step("Check meme id is {expected_id}")
    def check_meme_id(self, expected_id):
        self.check_field_exists("id")
        assert int(self.json["id"]) == int(expected_id), (
            f"Expected meme id {expected_id}, got {self.json['id']}"
        )

    @allure.step("Check meme data matches payload")
    def check_meme_matches_payload(self, payload):
        for field in ("text", "url", "tags", "info"):
            self.check_field_value(field, payload[field])
