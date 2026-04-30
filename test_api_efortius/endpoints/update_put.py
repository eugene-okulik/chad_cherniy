import allure
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


class UpdatePut(BaseEndpoint):
    @allure.step('Update Put')
    def update_put(self, payload, obj_id):
        return self._request("PUT", f"/object/{obj_id}", payload=payload)
