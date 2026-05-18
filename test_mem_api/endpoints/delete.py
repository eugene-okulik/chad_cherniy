import logging
import allure
from test_mem_api.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class DeleteMeme(BaseEndpoint):
    @allure.step("Delete meme with id {meme_id}")
    def delete_meme(self, meme_id, token=None):
        logger.info("Deleting meme with id %s", meme_id)
        return self._request("DELETE", f"/meme/{meme_id}", token=token)
