from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import (
    Column,
    Integer,
    String,
)


SQLALCHEMY_DATABASE_URL = "sqlite:///./instance/test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def save_user(session: Session, user: User) -> None:
    session.add(user)
    session.commit()