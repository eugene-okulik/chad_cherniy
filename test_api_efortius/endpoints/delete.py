import allure
import logging
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class DeleteObject(BaseEndpoint):
    @allure.step('Delete Object with ID {obj_id}')
    def delete_obj(self, obj_id):
        logger.info("Deleting object with id %s", obj_id)
        return self._request("DELETE", f"/object/{obj_id}")
