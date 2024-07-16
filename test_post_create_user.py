import requests
from assertpy import assert_that
from colorama import init, Fore
from configurations import users_api_url
import pytest

# Initialize colorama
init()


@pytest.mark.regression()
def test_user_creation():
    name = "Vasya"
    job = "assasin"

    name_entry = {"name": name}
    job_entry = {"job": job}

    # creation_user_data = {{"name": name}, {"job": job}}
    #
    # creation_user_data = { **name_entry, **job_entry}
    creation_user_data = name_entry | job_entry
    print(Fore.LIGHTCYAN_EX + f"creation_user_data: {creation_user_data}")

    response = requests.post(
        url=f"{users_api_url}",
        json=creation_user_data
    )

    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.ok).is_equal_to(True)
    assert_that(response.reason).is_equal_to("Created")

    json_response = response.json()
    print(Fore.RED + json_response["name"])
    print(Fore.RED + json_response["id"])
    assert_that(response.json()["name"]).is_equal_to(name)
    assert_that(json_response["job"]).is_equal_to(job)
    assert_that(json_response).contains_entry(name_entry)
    assert_that(json_response).contains_entry(job_entry)
