import os
import requests
import allure
from dotenv import load_dotenv
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


load_dotenv()


class UpdatePatch(BaseEndpoint):
    url = os.getenv('MAIN_URL')

    @allure.step('Update Patch')
    def update_patch(self, body, obj_id):
        self.response = (requests.patch(
            f"{self.url}/object/{obj_id}",
            timeout=20,
            json=body,
        ))
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response
