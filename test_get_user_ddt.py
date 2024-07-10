import requests
from assertpy import assert_that
from configurations import users_api_url
import pytest

#https://reqres.in/api/users
#id	1
#email	"george.bluth@reqres.in"
#first_name	"George"

testing_data = [
    (1, "george.bluth@reqres.in", "George"),
    (2, "janet.weaver@reqres.in", "Janet"),
    (3, "emma.wong@reqres.in", "Emma"),
    (4, "eve.holt@reqres.in", "Eve"),
    (5, "charles.morris@reqres.in", "Charles")
]

@pytest.mark.parametrize("user_id, user_email, user_first_name", testing_data)
def test_get_user_and_validate_data(user_id, user_email, user_first_name):
    response = requests.get(f"{users_api_url}/{user_id}")
    assert_that(response.status_code).is_equal_to(200)
    assert response.ok == True
    json_responce_data = response.json()['data']
    assert_that(json_responce_data["id"]).is_equal_to(user_id)
    assert_that(json_responce_data["email"]).is_equal_to(user_email)
    assert_that(json_responce_data["first_name"]).is_equal_to(user_first_name)
