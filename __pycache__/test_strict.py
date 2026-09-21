import pytest

@pytest.mark.nonexistent_marker
def teat_bad_maker():
    assert True