import pytest
from test_mem_api.endpoints.autorize import AuthorizeMeme


mem1 = "https://i.pinimg.com/736x/1a/da/ff/1adaff93a47735aa8caae77e85a78edd.jpg"


@pytest.mark.authorization
def test_auth(take_authorization_endpoint):
    payload = {"name": "Test"}

    take_authorization_endpoint.authorize(payload)
    take_authorization_endpoint.check_status_code(200)
    print(take_authorization_endpoint.json["token"])
