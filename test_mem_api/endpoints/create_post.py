import allure
import logging
from test_mem_api.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class PostMeme(BaseEndpoint):
    @allure.step('Create new meme post')
    def create_new_mem(self, payload, headers=None):
        logger.info("Creating new mem")
        return self._request("POST", "/meme", payload=payload, headers=headers)
