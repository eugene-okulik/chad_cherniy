import pytest
import logging
from test_mem_api.endpoints.create_post import PostMeme
from test_mem_api.endpoints.autorize import AuthorizeMeme


logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def take_authorization_endpoint():
    return AuthorizeMeme()


@pytest.fixture(scope="function")
def meme_post_endpoint():
    return PostMeme()


@pytest.fixture(scope="function")
def get_mem_endpoint():
    return GetMeme()


@pytest.fixture(scope="function")
def meme_put_endpoint():
    return PutMeme()


@pytest.fixture(scope="function")
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture(scope="function")
def created_mem(meme_post_endpoint):
    payload = {"name": "TestObj", "data": {"temp": True}}
    logger.info(f"Тело объекта: {payload}")

    logger.info("Создаем новый объект")
    meme_post_endpoint.create_new_mem(payload)
    response = meme_post_endpoint.json

    logger.debug(f"Получен ответ: {response}")
    meme_post_endpoint.check_status_code(200)

    yield response


@pytest.fixture(scope="function")
def authorization():
    payload = {"name": "TestObj"}
    logger.info(f"Имя: {payload}")

    logger.info("Проходим авторизацию")
    authorize_endpoint = AuthorizeMeme()
    authorize_endpoint.authorize(payload)

    logger.debug(f"Получен ответ: {authorize_endpoint.json}")
    authorize_endpoint.check_status_code(200)

    yield authorize_endpoint.json["token"]
