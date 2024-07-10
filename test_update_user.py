import requests
from assertpy import assert_that
from colorama import init, Fore
from configurations import users_api_url


def test_update_user_with_put():
    name = 'Vasya'
    update_user_data = {
        "name": name
    }
    response = requests.put(
        f"{users_api_url}/2",
        json=update_user_data
    )
    json_response = response.json()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.reason).is_equal_to("OK")
    assert_that(json_response).contains_key("name")
    assert_that(json_response["name"]).is_equal_to(name)


def test_update_user_with_patch():
    name = 'Petro'
    job = 'traktorist'
    update_user_data = {
        "name": name,
        "job": job
    }
    response = requests.patch(
        f"{users_api_url}/2",
        json=update_user_data
    )
    json_response = response.json()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.reason).is_equal_to("OK")
    assert_that(json_response).contains_key("name")
    assert_that(json_response).contains_key("job")
    assert_that(json_response).contains_key("updatedAt")
    assert_that(json_response["name"]).is_equal_to(name)
    assert_that(json_response["job"]).is_equal_to(job)
