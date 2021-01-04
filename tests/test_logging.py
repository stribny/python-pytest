import logging
import pytest
from python_pytest.logging import log_iterations


def test_iterations_logged(caplog):
    # given
    n_iterations = 10
    caplog.set_level(logging.DEBUG)

    # when
    log_iterations(n_iterations)

    # then
    assert len(caplog.records) == n_iterations
    assert caplog.records[0].message == "Iteration i=0"
    assert caplog.records[0].levelname == "INFO"
    assert caplog.records[9].message == "Iteration i=9"
    assert caplog.records[9].levelname == "INFO"


def test_iterations_exception_logged(caplog):
    # given
    n_iterations = -1
    caplog.set_level(logging.DEBUG)

    # when
    with pytest.raises(ValueError):
        log_iterations(n_iterations)

    # then
    assert caplog.records[0].message == "Iterations couldnt be logged"
    assert caplog.records[0].exc_info[0] is ValueError