import pytest


def test_1():
    ...


@pytest.mark.slow
def test_2():
    ...


@pytest.mark.skip
def test_3():
    ...