import allure
import pytest
import logging
from test_api_efortius.endpoints.create_post import CreatePost


logger = logging.getLogger(__name__)


# POST /object - создание объекта
@pytest.mark.critical
@pytest.mark.parametrize(
    'people', [
        {"name": "Vin", "data": {"second_name": "Diezel", "age": 31}},
        {"name": "Vin2", "data": {"second_name": "Diezel2", "age": 32}},
        {"name": "Vin3", "data": {"second_name": "Diezel3", "age": 33}}
    ]
)
def test_create_object(people):
    logger.info(f"Начинаем создание объекта: {people['name']}")
    with allure.step('Create object'):
        body = {
            "name": people["name"],
            "data": people["data"]
        }
    with allure.step('Send request'):
        create_object = CreatePost()
        create_object.new_post(body)
        response = create_object.json
        logger.debug(f"Получен ответ: {response}")
    with allure.step('Check response'):
        actual_status = create_object.response.status_code if hasattr(create_object,
            'response') else create_object.status_code
        logger.info(f"🔍 Ожидаемый статус: 200, Фактический: {actual_status}")
        assert actual_status == 200, f'Created: ожидался 200, получено {actual_status}'
