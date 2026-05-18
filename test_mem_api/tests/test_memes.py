import pytest


@pytest.mark.critical
def test_create_meme(meme_post_endpoint, meme_payload, auth_token):
    meme_post_endpoint.create_new_mem(meme_payload, auth_token)
    meme_post_endpoint.check_status_code(200)
    meme_post_endpoint.check_meme_matches_payload(meme_payload)


@pytest.mark.critical
def test_get_created_meme(get_meme_endpoint, created_meme, auth_token):
    get_meme_endpoint.get_meme_by_id(created_meme["id"], auth_token)
    get_meme_endpoint.check_status_code(200)
    get_meme_endpoint.check_meme_id(created_meme["id"])


@pytest.mark.medium
def test_created_meme_in_memes_list(get_meme_endpoint, created_meme, auth_token):
    get_meme_endpoint.get_all_memes(auth_token)
    get_meme_endpoint.check_status_code(200)



@pytest.mark.critical
def test_update_meme(meme_put_endpoint, get_meme_endpoint, created_meme, updated_meme_payload, auth_token):
    updated_meme_payload["id"] = created_meme["id"]

    meme_put_endpoint.update_meme(created_meme["id"], updated_meme_payload, auth_token)
    meme_put_endpoint.check_status_code(200)
    meme_put_endpoint.check_meme_id(created_meme["id"])
    meme_put_endpoint.check_meme_matches_payload(updated_meme_payload)

    get_meme_endpoint.get_meme_by_id(created_meme["id"], auth_token)
    get_meme_endpoint.check_status_code(200)
    get_meme_endpoint.check_meme_matches_payload(updated_meme_payload)


@pytest.mark.critical
def test_delete_meme(
    meme_post_endpoint,
    delete_meme_endpoint,
    get_meme_endpoint,
    meme_payload,
    auth_token,
):
    meme_post_endpoint.create_new_mem(meme_payload, auth_token)
    meme_post_endpoint.check_status_code(200)
    meme_id = meme_post_endpoint.json["id"]

    delete_meme_endpoint.delete_meme(meme_id, auth_token)
    delete_meme_endpoint.check_status_code(200)

    get_meme_endpoint.get_meme_by_id(meme_id, auth_token)
    get_meme_endpoint.check_status_code(404)


@pytest.mark.medium
def test_meme_endpoints_require_authorization(meme_post_endpoint, get_meme_endpoint, meme_payload):
    meme_post_endpoint.create_new_mem(meme_payload)
    meme_post_endpoint.check_status_code(401)

    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_status_code(401)
