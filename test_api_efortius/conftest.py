import pytest
import allure
import logging
from test_api_efortius.endpoints.create_post import CreatePost
from test_api_efortius.endpoints.delete import DeleteObject


logger = logging.getLogger(__name__)


@allure.step('Create test obj')
@pytest.fixture(scope="function")
def created_object():
    payload = {"name": "TestObj", "data": {"temp": True}}
    logger.info(f"Тело объекта: {payload}")

    logger.info("Создаем новый объект")
    create_object = CreatePost()
    create_object.new_post(payload)
    response = create_object.json

    logger.debug(f"Получен ответ: {response}")
    create_object.check_status_code(200)

    yield response

    logger.info("Удаляем тестовый объект")
    delete_object = DeleteObject()
    delete_object.delete_obj(response["id"])
    delete_object.check_status_code((200, 404))
