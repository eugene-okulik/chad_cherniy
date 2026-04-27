import allure
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    @allure.step('Delete Object with ID {obj_id}')
    def delete_obj(self, obj_id):
        return self._request("DELETE", f"/object/{obj_id}")
