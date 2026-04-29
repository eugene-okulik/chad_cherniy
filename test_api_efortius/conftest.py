import pytest
import logging
from test_api_efortius.endpoints.create_post import CreatePost
from test_api_efortius.endpoints.delete import DeleteObject
from test_api_efortius.endpoints.update_patch import UpdatePatch
from test_api_efortius.endpoints.update_put import UpdatePut


logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def create_post_endpoint():
    return CreatePost()


@pytest.fixture(scope="function")
def update_put_endpoint():
    return UpdatePut()


@pytest.fixture(scope="function")
def update_patch_endpoint():
    return UpdatePatch()


@pytest.fixture(scope="function")
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture(scope="function")
def created_object(create_post_endpoint, delete_object_endpoint):
    payload = {"name": "TestObj", "data": {"temp": True}}
    logger.info(f"Тело объекта: {payload}")

    logger.info("Создаем новый объект")
    create_post_endpoint.create_new_post(payload)
    response = create_post_endpoint.json

    logger.debug(f"Получен ответ: {response}")
    create_post_endpoint.check_status_code(200)

    yield response

    # logger.info("Удаляем тестовый объект")
    # delete_object_endpoint.delete_obj(response["id"])
    # delete_object_endpoint.check_status_code((200, 404))
