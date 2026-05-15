import allure
import logging
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class CreatePost(BaseEndpoint):
    @allure.step('Create new object')
    def create_new_obj(self, payload, headers=None):
        logger.info("Creating new object")
        return self._request("POST", "/object", payload=payload, headers=headers)
