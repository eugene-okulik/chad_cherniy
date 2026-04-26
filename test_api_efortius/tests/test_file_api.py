import allure
import pytest
import logging
from test_api_efortius.endpoints.create_post import CreatePost


logger = logging.getLogger(__name__)


# POST /object - создание объекта
@pytest.mark.critical
@pytest.mark.parametrize(
    'people', [
        {"name": "Vin11", "data": {"second_name": "Diezel11", "age": 131}},
        {"name": "Vin12", "data": {"second_name": "Diezel12", "age": 132}},
        {"name": "Vin13", "data": {"second_name": "Diezel13", "age": 33}}
    ]
)
def test_create_object(people):
    logger.info(f"Начинаем создание объекта: {people['name']}")
    with allure.step('Create object'):
        body = {
            "name": people["name"],
            "data": people["data"]
        }
    create_object = CreatePost()
    create_object.new_post(body)
    response = create_object.json
    logger.debug(f"Получен ответ: {response}")

    with allure.step('Check response'):
        create_object.check_status_code(200)
        assert response["name"] == people["name"]
        assert response["data"] == people["data"]
