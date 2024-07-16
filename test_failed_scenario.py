import pytest

# additional option for bug skiping
@pytest.mark.xfail(reason="Unknown bug - curently example")
def test_failed_assertation():
    assert 2 + 5 == 6
