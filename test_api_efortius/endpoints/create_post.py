import allure
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


class CreatePost(BaseEndpoint):
    @allure.step('Create new Post')
    def create_new_post(self, payload, headers=None):
        return self._request("POST", "/object", payload=payload, headers=headers)
