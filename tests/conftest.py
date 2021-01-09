import pytest
from python_pytest.db_interaction import User, Base, engine, get_session


def db_set_up(session):
    Base.metadata.create_all(bind=engine)


def db_tear_down(session):
    session.query(User).delete()
    session.commit()
    session.remove()


@pytest.fixture
def session():
    session = get_session()
    db_set_up(session)
    yield session
    db_tear_down(session)