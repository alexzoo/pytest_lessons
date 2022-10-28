
from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_posts(get_users):
    Response(get_users).assert_status_code(200).validate(User)



