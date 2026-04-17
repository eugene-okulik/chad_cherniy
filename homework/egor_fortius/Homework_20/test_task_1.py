from dotenv import load_dotenv
import requests
from icecream import ic
import os
import pytest


load_dotenv()

base_url = os.getenv("MAIN_URL")


@pytest.fixture(scope="function")
def start_end_text():
    ic('before test')
    yield
    ic('after test')


@pytest.fixture(scope="session")
def info():
    ic("Start testing")
    yield
    ic("Testing completed")


@pytest.fixture(scope="function")
def created_object():
    # Создаём объект
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


def test_all_objects(info, start_end_text):
    response = requests.get(f"{base_url}/object", timeout=20)
    assert response.status_code == 200, 'Not Success'
    # data = response.json()
    # ic(data)


# POST /object - создание объекта
@pytest.mark.critical
@pytest.mark.parametrize(
    'people', [
        {"name": "Vin", "data": {"second_name": "Diezel", "age": 31}},
        {"name": "Vin2", "data": {"second_name": "Diezel2", "age": 32}},
        {"name": "Vin3", "data": {"second_name": "Diezel3", "age": 33}}
    ]
)
def test_create_object(start_end_text, people):
    body = {
        "name": people["name"],
        "data": people["data"]
    }
    response = requests.post(
        f"{base_url}/object", timeout=20,
        json=body,
    )
    assert response.status_code == 200, 'Created'
    result = response.json()
    ic(result)


# PUT /object/<id> — полное обновление
def test_put_object(start_end_text, created_object):
    obj_id = created_object["id"]
    
    body = {
        "name": "Shaman The Great",
        "data": {"second_name": "Really", "age": 19}
    }
    response = requests.put(
        f"{base_url}/object/{obj_id}",
        timeout=20,
        json=body,
    )
    assert response.status_code == 200, f'PUT failed: {response.status_code}'
    data = response.json()
    
    assert int(data["id"]) == obj_id
    assert data["name"] == body["name"]
    assert data["data"] == body["data"]


# PATCH /object/<id> — частичное обновление
def test_patch_object(start_end_text, created_object):
    obj_id = created_object["id"]
    
    body = {"name": "Gondurasina"}
    response = requests.patch(
        f"{base_url}/object/{obj_id}",
        json=body,
        timeout=20
    )
    assert response.status_code == 200, f'PATCH failed: {response.status_code}'
    result = response.json()
    
    assert result["name"] == "Gondurasina"
    
    ic(f"✏️ PATCH обновлён объект #{obj_id}: {result['name']}")


# DELETE /object/<id> — удаление
def test_delete_object(start_end_text, created_object):
    obj_id = created_object["id"]
    
    response = requests.delete(
        f"{base_url}/object/{obj_id}",
        timeout=20
    )
    assert response.status_code == 200, f'DELETE failed: {response.status_code}'
    ic(f"🗑️ Объект #{obj_id} удалён (200)")
    
    # Проверяем, что объект действительно удалён
    check = requests.get(f"{base_url}/object/{obj_id}", timeout=10)
    assert check.status_code == 404, "Объект должен быть удалён"
    ic(f"✅ Подтверждено: объект #{obj_id} не найден (404)")
