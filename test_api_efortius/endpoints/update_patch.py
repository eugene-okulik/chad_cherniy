import allure
import logging
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


logger = logging.getLogger(__name__)


class UpdatePatch(BaseEndpoint):
    @allure.step('Update Patch')
    def update_patch(self, payload, obj_id):
        logger.info("Updating object with PATCH: %s", obj_id)
        return self._request("PATCH", f"/object/{obj_id}", payload=payload)
