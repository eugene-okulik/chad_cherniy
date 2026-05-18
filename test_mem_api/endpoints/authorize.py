import logging
import allure
from test_mem_api.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class AuthorizeMeme(BaseEndpoint):
    @allure.step("Authorize user")
    def authorize(self, payload):
        logger.info("Authorizing user")
        return self._request(
            "POST",
            "/authorize",
            payload=payload,
            headers={"Content-Type": "application/json"},
        )

    @allure.step("Check token is alive")
    def check_token(self, token):
        logger.info("Checking token")
        return self._request("GET", f"/authorize/{token}")

    @allure.step("Check authorization response contains token")
    def check_token_received(self):
        self.check_field_exists("token")
