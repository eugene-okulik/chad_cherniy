import logging
import allure
from test_mem_api.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class PostMeme(BaseEndpoint):
    @allure.step("Create new meme")
    def create_new_mem(self, payload, token=None):
        logger.info("Creating new meme")
        return self._request("POST", "/meme", payload=payload, token=token)
