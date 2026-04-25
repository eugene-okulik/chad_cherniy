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
    with allure.step('Create object'):
        body = {
            "name": people["name"],
            "data": people["data"]
        }
    with allure.step('Send request'):
        create_object = CreatePost()
        create_object.new_post(body)
        response = create_object.json
        print(response)
    with allure.step('Check response'):
        assert create_object.status_code == 200, 'Created'
