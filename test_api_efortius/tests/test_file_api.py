import pytest
import logging


logger = logging.getLogger(__name__)


TEST_DATA = [
    {"name": "Viki", "data": {"second_name": "Piki", "age": 18}},
    {"name": "June", "data": {"second_name": "Mune", "age": 19}},
    {"name": "Margo", "data": {"second_name": "Fargo", "age": 20}}
]


# POST /object - создание объекта
@pytest.mark.critical
@pytest.mark.parametrize('people', TEST_DATA)
def test_create_object(people, create_post_endpoint):
    create_post_endpoint.create_new_obj(payload=people)
    create_post_endpoint.check_status_code(200)
    create_post_endpoint.check_field_value("name", people["name"])
    create_post_endpoint.check_field_value("data", people["data"])


# PUT /object/<id> — полное обновление
@pytest.mark.medium
def test_put_object(created_object, update_put_endpoint):
    obj_id = created_object["id"]

    payload = {
        "name": "Vishnya",
        "data": {"second_name": "Shaman", "age": 21}
    }

    update_put_endpoint.update_put(payload, obj_id)
    update_put_endpoint.check_status_code(200)
    update_put_endpoint.check_object_id(obj_id)
    update_put_endpoint.check_field_value("name", payload["name"])
    update_put_endpoint.check_field_value("data", payload["data"])


# PATCH /object/<id> — частичное обновление
@pytest.mark.medium
def test_patch_object(created_object, update_patch_endpoint):
    obj_id = created_object["id"]

    payload = {"name": "Plazenia"}

    update_patch_endpoint.update_patch(payload, obj_id)
    update_patch_endpoint.check_status_code(200)
    update_patch_endpoint.check_field_value("name", payload["name"])


# DELETE /object/<id> — удаление
@pytest.mark.critical
def test_delete_object(created_object, delete_object_endpoint):
    obj_id = created_object["id"]

    delete_object_endpoint.delete_obj(obj_id)
    delete_object_endpoint.check_status_code(200)
