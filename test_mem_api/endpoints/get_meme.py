import logging
import allure
from test_mem_api.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class GetMeme(BaseEndpoint):
    @allure.step("Get all memes")
    def get_all_memes(self, token=None):
        logger.info("Getting all memes")
        return self._request("GET", "/meme", token=token)

    @allure.step("Get meme by id {meme_id}")
    def get_meme_by_id(self, meme_id, token=None):
        logger.info("Getting meme with id %s", meme_id)
        return self._request("GET", f"/meme/{meme_id}", token=token)
