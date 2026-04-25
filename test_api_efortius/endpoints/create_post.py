import os
import requests
from dotenv import load_dotenv


load_dotenv()


class CreatePost:
    url = os.getenv('MAIN_URL')
    response = None
    status_code = None
    json = None

    def new_post(self, body):
        self.response = requests.post(
            f"{self.url}/object",
            timeout=20,
            json=body,
        )
        self.json = self.response.json()
        self.status_code = self.response.status_code
        return self.response
