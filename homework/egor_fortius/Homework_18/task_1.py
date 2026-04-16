import requests
from icecream import ic


MAIN_URL = 'http://objapi.course.qa-practice.com/'

def all_objects():
    response = requests.get(f"{MAIN_URL}/object")
    assert response.status_code == 200, 'Resurs not found'

# result = all_objects()

def creat_object():
    body = {
        "name": "Isaak",
        "data": {"second_name": "Newtooon", "age": 23},
    }
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(f"{MAIN_URL}/object",
        json=body,
        headers=headers
    )
    assert resp.status_code == 200, 'Status code is incorrect'

new_obj = creat_object()
