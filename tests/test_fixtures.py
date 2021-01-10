from python_pytest import fixtures


def test_allowed_names(allowed_names):
    # when
    name = fixtures.get_allowed_name()

    # then
    assert name in allowed_names