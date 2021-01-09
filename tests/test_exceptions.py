import pytest
from python_pytest import exceptions


@pytest.mark.parametrize("exc", [(ValueError), (ImportError), (IndexError)])
def test_raise_exc(exc):
    with pytest.raises(exc):
        exceptions.raise_exc(exc)
    