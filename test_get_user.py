import requests
from assertpy import assert_that
from configurations import users_api_url


def test_get_user_status_code_and_ok():
    response = requests.get(f"https://reqres.in/api/users/2")
    assert response.status_code == 200
    assert_that(response.status_code).is_equal_to(200)
    assert response.ok == True
    assert_that(response.ok).is_true()


def test_get_user_id():
    id = 2
    response = requests.get(f"https://reqres.in/api/users/{id}")
    json_response = response.json()

    assert_that(json_response).contains_key("data")
    assert_that(json_response).contains_key("support")

    assert_that(json_response["data"]["id"]).is_equal_to(id)
    assert json_response["data"]["id"] == id
