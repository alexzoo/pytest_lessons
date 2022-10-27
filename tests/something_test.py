import requests

from configuration import SERVICE_URL
from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200)


def test_getting_users():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)
