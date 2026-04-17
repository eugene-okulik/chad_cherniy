from dotenv import load_dotenv
import requests
from icecream import ic
import os
import pytest


load_dotenv()

base_url = os.getenv("MAIN_URL")

@pytest.fixture()
def start_end_text():
    ic('\nbefore test')
    yield
    ic('\nafter test')

@pytest.fixture(scope="session")
def info():
    ic("\nStart testing")
    yield
    ic("\nTesting completed")

def test_all_objects(start_end_text):
    response = requests.get(f"{base_url}/object", timeout=20)
    assert response.status_code == 200, 'Not Success'
    # data = response.json()
    # ic(data)

@pytest.mark.critical
@pytest.mark.parametrize(
    'people', [
        {"name": "Vin", "data": {"second_name": "Diezel", "age": 31}},
        {"name": "Vin2", "data": {"second_name": "Diezel2", "age": 32}},
        {"name": "Vin3", "data": {"second_name": "Diezel3", "age": 33}}
        ]
    )
# POST /object - создание объекта
def test_create_object(start_end_text, info, people):
    body = {
        "name": people["name"],
        "data": people["data"]
    }
    response = requests.post(
        f"{base_url}/object", timeout=20,
        json=body,
    )
    assert response.status_code == 201, 'Created'
    result = response.json()
    ic(result)
    return result


# PUT /object/<id> — полное обновление
def test_put_obj(start_end_text, obj_id):
    body = {
        "name": "Shaman The Great",
        "data": {"second_name": "Really", "age": 19}
    }
    response = requests.put(
        f"{base_url}/object/{obj_id}",
        json=body,
    )
    assert response.status_code == 200, 'Not Success'
    data = response.json()
    assert data["id"] == obj_id
    ic(data)


# PATCH /object/<id> — частичное обновление
def test_update_object_patch(start_end_text, obj_id):
    body = {"name": "Gondurasina"}
    response = requests.patch(f"{base_url}/object/{obj_id}", json=body, timeout=20)
    assert response.status_code == 200
    result = response.json()
    ic(result)
    return result


# DELETE /object/<id> — удаление
def test_delete_object(start_end_text, obj_id):
    response = requests.delete(f"{base_url}/object/{obj_id}")
    assert response.status_code == 204
    ic(f"✅ Объект {obj_id} удалён (204)")
    return True


# ЗАПУСК СЦЕНАРИЯ
if __name__ == "__main__":


    # 1. Создаём объект и сразу получаем его ID
    new_obj = test_create_object()
    obj_id = new_obj["id"]
    ic(f"Создан объект с ID: {obj_id}")

    # 2.
    test_put_obj(obj_id)
    test_update_object_patch(obj_id)
    test_delete_object(obj_id)

    # 3. Проверяем, что объект действительно удалён
    response = requests.get(f"{base_url}/object/{obj_id}", timeout=10)
    assert response.status_code == 404, "Объект должен быть удалён"
