import pytest
from python_pytest.asserts import add


@pytest.mark.parametrize("num,num2,result", [
    (10, 20, 30),
    (25, 25, 50),
    (11, 19, 30)
])
def test_add_can_add_numbers(num, num2, result):
    assert add(num, num2) == result