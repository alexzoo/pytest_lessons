import pytest

from src.base_classes.response import Response
from src.generators.player_localization import PlayerLocalization
from src.schemas.user import User


@pytest.mark.dev
def test_getting_posts(get_users):
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    ('a', 'b', 'ab')
])
def test_calculate(first_value, second_value, result):
    assert (first_value + second_value) == result


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_statuses(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('balance', [
    '100',
    '0',
    '-100',
    'trololo'
])
def test_balance(balance, get_player_generator):
    print(get_player_generator.set_balance(balance).build())


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_delete_key(delete_key, get_player_generator):
    object_to_test = get_player_generator.build()
    del object_to_test[delete_key]
    print(object_to_test)


def test_inner_generator(get_player_generator):
    object_to_test = get_player_generator.update_inner_value(
        ['localize', 'fr', 'is', 'best'], PlayerLocalization('fr_FR')
    ).build()
    print(object_to_test)
