import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def log_iterations(n_iterations: int) -> None:
    try:
        if n_iterations < 0:
            raise ValueError("Number of iterations cannot be negative")
        for i in range(n_iterations):
            logger.info('Iteration i=%d', i)
    except ValueError as ex:
        logger.exception("Iterations couldnt be logged", exc_info=True)
        raise ex