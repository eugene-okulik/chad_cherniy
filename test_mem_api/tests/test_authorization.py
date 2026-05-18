import pytest


@pytest.mark.authorization
def test_saved_authorization_token_is_alive(authorization_endpoint, auth_token):
    authorization_endpoint.check_token(auth_token)
    authorization_endpoint.check_status_code(200)
