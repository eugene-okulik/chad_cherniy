import os
import requests
import allure
from dotenv import load_dotenv
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


load_dotenv()


class DeleteObject(BaseEndpoint):
    url = os.getenv('MAIN_URL')

    @allure.step('Delete Object with ID {obj_id}')
    def delete_obj(self, obj_id):
        self.response = (requests.delete(
            f"{self.url}/object/{obj_id}",
            timeout=20
        ))
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response
