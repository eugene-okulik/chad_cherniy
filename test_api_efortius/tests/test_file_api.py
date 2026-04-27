import pytest
import logging
from test_api_efortius.endpoints.create_post import CreatePost
from test_api_efortius.endpoints.delete import DeleteObject
from test_api_efortius.endpoints.update_patch import UpdatePatch
from test_api_efortius.endpoints.update_put import UpdatePut


logger = logging.getLogger(__name__)


TEST_DATA = [
    {"name": "Viki", "data": {"second_name": "Piki", "age": 18}},
    {"name": "June", "data": {"second_name": "Mune", "age": 19}},
    {"name": "Margo", "data": {"second_name": "Fargo", "age": 20}}
]


# POST /object - создание объекта
@pytest.mark.critical
@pytest.mark.parametrize('people', TEST_DATA)
def test_create_object(people):
    logger.info(f"Начинаем создание объекта: {people['name']}")

    create_object = CreatePost()
    create_object.new_post(payload=people)
    response = create_object.json

    logger.debug(f"Получен ответ: {response}")
    create_object.check_status_code(200)

    assert response["name"] == people["name"]
    assert response["data"] == people["data"]


# PUT /object/<id> — полное обновление
@pytest.mark.medium
def test_put_object(created_object):
    logger.info("Обновление объекта полное")
    obj_id = created_object["id"]

    body = {
        "name": "Vishnya",
        "data": {"second_name": "Shaman", "age": 21}
    }

    update_object = UpdatePut()
    update_object.update_put(body, obj_id)
    response = update_object.json

    logger.debug(f"Получен ответ: {response}")
    update_object.check_status_code(200)

    assert int(response["id"]) == obj_id
    assert response["name"] == body["name"]
    assert response["data"] == body["data"]


# PATCH /object/<id> — частичное обновление
@pytest.mark.medium
def test_patch_object(created_object):
    logger.info("Обновление объекта частичное")
    obj_id = created_object["id"]

    body = {"name": "Plazenia"}

    update_object = UpdatePatch()
    update_object.update_patch(body, obj_id)
    response = update_object.json

    logger.debug(f"Получен ответ: {response}")
    update_object.check_status_code(200)

    assert response["name"] == "Plazenia"


# DELETE /object/<id> — удаление
@pytest.mark.critial
def test_delete_object(created_object):
    obj_id = created_object["id"]

    delete_object = DeleteObject()
    delete_object.delete_obj(obj_id)

    logger.debug(f"Получен ответ statuscode: {delete_object.status_code}")
    delete_object.check_status_code(200)
