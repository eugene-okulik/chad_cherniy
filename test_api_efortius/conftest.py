import pytest
import logging
from test_api_efortius.endpoints.create_post import CreatePost


logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def created_object():
    body = {"name": "TestObj", "data": {"temp": True}}
    logger.info(f"Тело объекта: {body}")

    logger.info("Создаем новый объект")
    create_object = CreatePost()
    create_object.new_post(body)
    response = create_object.json
    logger.debug(f"Получен ответ: {response}")

    create_object.check_status_code(200)

    yield response
