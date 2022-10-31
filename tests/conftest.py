import pytest
import requests

from configuration import SERVICE_URL
from src.generators.player import Player


@pytest.fixture
def get_users():
    return requests.get(url=SERVICE_URL)


@pytest.fixture
def get_player_generator():
    return Player()
