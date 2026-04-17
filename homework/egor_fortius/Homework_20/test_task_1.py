from dotenv import load_dotenv
import requests
from icecream import ic
import os

load_dotenv()

base_url = os.getenv("MAIN_URL")

def test_all_objects():
    response = requests.get(f"{base_url}/object", timeout=20)
    assert response.status_code == 200, 'Not Success'
    data = response.json()
    ic(data)


# POST /object - создание объекта
def test_create_object():
    body = {
        "name": "Genrih",
        "data": {"second_name": "VIII", "age": 32}
    }
    response = requests.post(
        f"{base_url}/object", timeout=20,
        json=body,
    )
    assert response.status_code == 200, 'Not Success'
    result = response.json()
    ic(result)
    return result


# PUT /object/<id> — полное обновление
def test_put_obj(obj_id):
    body = {
        "name": "Genrih XII",
        "data": {"second_name": "Perdu", "age": 32}
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
def test_update_object_patch(obj_id):
    body = {"name": "Gondurasina"}
    response = requests.patch(f"{base_url}/object/{obj_id}", json=body, timeout=20)
    assert response.status_code == 200
    result = response.json()
    ic(result)
    return result


# DELETE /object/<id> — удаление
def test_delete_object(obj_id):
    response = requests.delete(f"{base_url}/object/{obj_id}")
    assert response.status_code == 204
    ic(f"✅ Объект {obj_id} удалён (204)")
    return True


# ЗАПУСК СЦЕНАРИЯ
if __name__ == "__main__":
    ic("Начинаем тестирование API")

    # 1. Создаём объект и сразу получаем его ID
    new_obj = create_object()
    obj_id = new_obj["id"]
    ic(f"Создан объект с ID: {obj_id}")

    # 2.
    put_obj(obj_id)
    update_object_patch(obj_id)
    delete_object(obj_id)

    # 3. Проверяем, что объект действительно удалён
    response = requests.get(f"{base_url}/object/{obj_id}", timeout=10)
    assert response.status_code == 404, "Объект должен быть удалён"

    ic("Все тесты прошли успешно!")
