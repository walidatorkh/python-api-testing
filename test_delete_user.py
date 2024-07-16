import requests
from assertpy import assert_that
from colorama import init, Fore
from configurations import base_url
import pytest


# option to skip specific test
# @pytest.mark.skip(reason="DEleting users is not working")
@pytest.mark.regression()
def test_user_deletion():
    response = requests.delete(f"{base_url}/api/register/552")

    assert_that(response.status_code).is_equal_to(204)
    assert_that(response.reason).is_equal_to_ignoring_case("no content")
