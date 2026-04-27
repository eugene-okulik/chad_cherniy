import os
import requests
import allure
from dotenv import load_dotenv
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


load_dotenv()


class UpdatePut(BaseEndpoint):
    url = os.getenv('MAIN_URL')

    @allure.step('Update Put')
    def update_put(self, body, obj_id):
        self.response = requests.put(
            f"{self.url}/object/{obj_id}",
            timeout=20,
            json=body,
        )
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response
