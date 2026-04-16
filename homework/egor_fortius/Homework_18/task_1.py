import requests
from icecream import ic

MAIN_URL = 'http://objapi.course.qa-practice.com/'

def all_objects():
    response = requests.get(f"{MAIN_URL}/object", timeout=10)
    assert response.status_code == 200, 'Not Success'
    data = response.json()
    ic(data)

result = all_objects()
