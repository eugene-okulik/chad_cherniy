import allure
import logging
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class UpdatePut(BaseEndpoint):
    @allure.step('Update Put')
    def update_put(self, payload, obj_id):
        logger.info("Updating object with PUT: %s", obj_id)
        return self._request("PUT", f"/object/{obj_id}", payload=payload)
