import allure
import pytest
import logging
from test_api_efortius.endpoints.create_post import CreatePost
from test_api_efortius.endpoints.update_put import UpdatePut

logger = logging.getLogger(__name__)


# POST /object - создание объекта
@pytest.mark.critical
@pytest.mark.parametrize(
    'people', [
        {"name": "Viki", "data": {"second_name": "Piki", "age": 18}},
        {"name": "June", "data": {"second_name": "Mune", "age": 19}},
        {"name": "Margo", "data": {"second_name": "Fargo", "age": 20}}
    ]
)
def test_create_object(people):
    logger.info(f"Начинаем создание объекта: {people['name']}")
    with allure.step('Создаём объект из body'):
        body = {
            "name": people["name"],
            "data": people["data"]
        }
    create_object = CreatePost()
    create_object.new_post(body)
    response = create_object.json
    logger.debug(f"Получен ответ: {response}")
    create_object.check_status_code(200)
    assert response["name"] == people["name"]
    assert response["data"] == people["data"]


# PUT /object/<id> — полное обновление
@pytest.mark.medium
def test_put_object(start_end_text, created_object):
    logger.info("Обновление объекта")
    obj_id = created_object["id"]

    body = {
        "name": "Ya Russkiy",
        "data": {"second_name": "Shaman", "age": 21}
    }
    update_object = UpdatePut()
    update_object.update_put(body)
    response = update_object.json
    logger.debug(f"Получен ответ: {response}")
    update_object.check_status_code(200)

    assert int(response["id"]) == obj_id
    assert response["name"] == body["name"]
    assert response["data"] == body["data"]