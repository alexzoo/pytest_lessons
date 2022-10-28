import pytest

from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_posts(get_users):
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    ('a', 'b', 'ab')
])
def test_calculate(first_value, second_value, result):
    assert (first_value + second_value) == result
