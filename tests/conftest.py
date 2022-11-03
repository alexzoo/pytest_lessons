import pytest
import requests

from configuration import SERVICE_URL
from database.db import Session
from src.generators.film_generator import FilmGenerator
from src.generators.player_generator import PlayerGenerator


@pytest.fixture
def get_users():
    return requests.get(url=SERVICE_URL)


@pytest.fixture
def get_player_generator():
    return PlayerGenerator()


@pytest.fixture
def get_film_generator():
    return FilmGenerator()


@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_data_from_table(session, table, filter_data):
    session.query(table).filter(filter_data).delete()
    session.commit()


@pytest.fixture
def get_delete_method():
    return delete_data_from_table


def add_method(session, item):
    session.add(item)
    session.commit()


@pytest.fixture
def get_add_method():
    return add_method

