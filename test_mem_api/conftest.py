import logging
from pathlib import Path
from uuid import uuid4

import pytest

from test_mem_api.endpoints.authorize import AuthorizeMeme
from test_mem_api.endpoints.create_post import PostMeme
from test_mem_api.endpoints.delete import DeleteMeme
from test_mem_api.endpoints.get_meme import GetMeme
from test_mem_api.endpoints.update_put import PutMeme


logger = logging.getLogger(__name__)
TOKEN_FILE = Path(__file__).with_name(".meme_token")


@pytest.fixture(scope="session")
def authorization_endpoint():
    return AuthorizeMeme()


@pytest.fixture(scope="session")
def auth_token(authorization_endpoint):
    token = _read_saved_token()
    if token and _token_is_alive(authorization_endpoint, token):
        return token

    payload = {"name": "Egor API tests"}
    authorization_endpoint.authorize(payload)
    authorization_endpoint.check_status_code(200)
    authorization_endpoint.check_token_received()

    token = authorization_endpoint.json["token"]
    TOKEN_FILE.write_text(token)
    return token


@pytest.fixture(scope="function")
def meme_post_endpoint():
    return PostMeme()


@pytest.fixture(scope="function")
def get_meme_endpoint():
    return GetMeme()


@pytest.fixture(scope="function")
def meme_put_endpoint():
    return PutMeme()


@pytest.fixture(scope="function")
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture(scope="function")
def meme_payload():
    unique_text = f"API meme {uuid4()}"
    return {
        "text": unique_text,
        "url": "https://i.pinimg.com/736x/1a/da/ff/1adaff93a47735aa8caae77e85a78edd.jpg",
        "tags": ["api", "pytest", "meme"],
        "info": {"course": "qa-practice", "type": "positive"},
    }


@pytest.fixture(scope="function")
def updated_meme_payload():
    return {
        "text": f"Updated API meme {uuid4()}",
        "url": "https://i.pinimg.com/736x/e4/3a/31/e43a31fbf4fdb0d4a32c8fce42cdb6d5.jpg",
        "tags": ["api", "pytest", "updated"],
        "info": {"course": "qa-practice", "type": "updated"},
    }


@pytest.fixture(scope="function")
def created_meme(meme_post_endpoint, delete_meme_endpoint, meme_payload, auth_token):
    meme_post_endpoint.create_new_mem(meme_payload, auth_token)
    meme_post_endpoint.check_status_code(200)
    meme_post_endpoint.check_meme_matches_payload(meme_payload)

    meme = meme_post_endpoint.json
    yield meme

    delete_meme_endpoint.delete_meme(meme["id"], auth_token)


def _read_saved_token():
    if not TOKEN_FILE.exists():
        return None
    return TOKEN_FILE.read_text().strip() or None


def _token_is_alive(authorization_endpoint, token):
    authorization_endpoint.check_token(token)
    return authorization_endpoint.response.status_code == 200
