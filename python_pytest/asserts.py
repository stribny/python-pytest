from python_pytest import asserts


def test_add_can_add_numbers():
    # given
    num = 3
    num2 = 45

    # when
    result = asserts.add(num, num2)

    # then
    assert result == 48