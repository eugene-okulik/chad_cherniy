import logging
import allure
from test_mem_api.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class PutMeme(BaseEndpoint):
    @allure.step("Update meme with PUT")
    def update_meme(self, meme_id, payload, token=None):
        logger.info("Updating meme with id %s", meme_id)
        return self._request("PUT", f"/meme/{meme_id}", payload=payload, token=token)
