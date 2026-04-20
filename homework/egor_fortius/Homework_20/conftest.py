import pytest
import requests
import os
from dotenv import load_dotenv
from icecream import ic


load_dotenv()

base_url = os.getenv("MAIN_URL")


@pytest.fixture(scope="function")
def created_object():
    # Создаём новый объект
    body = {"name": "TestObj", "data": {"temp": True}}
    response = requests.post(
        f"{base_url}/object",
        timeout=20,
        json=body
    )
    assert response.status_code == 200, f"Failed to create: {response.status_code}"
    obj = response.json()
    ic(f"📦 Fixture: создан объект #{obj['id']}")

    yield obj