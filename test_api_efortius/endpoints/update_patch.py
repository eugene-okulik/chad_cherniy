import allure
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


class UpdatePatch(BaseEndpoint):
    @allure.step('Update Patch')
    def update_patch(self, payload, obj_id):
        return self._request("PATCH", f"/object/{obj_id}", payload=payload)
