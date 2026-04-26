import os
import requests
import allure
from dotenv import load_dotenv
from test_api_efortius.endpoints.base_endpoint import BaseEndpoint


load_dotenv()


class CreatePost(BaseEndpoint):
    url = os.getenv('MAIN_URL')

    @allure.step('Create new Post')
    def new_post(self, body):
        self.response = requests.post(
            f"{self.url}/object",
            timeout=20,
            json=body,
        )
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response
