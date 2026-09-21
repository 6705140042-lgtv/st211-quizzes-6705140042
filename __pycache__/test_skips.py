import pytest
import sys

@pytest.mark.skip(reason="Feature not implemented")
def test_future_feature():
    assert False

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Require Python 3.8+")
def test_needs_modern_python():
     assert True