# from jsonschema import validate


class Response:

    """
    Полезный класс, который помогает нам экономить тонны кода в процессе
    валидации данных. На вход он принимает объект респонса и разбирает его.
    Вы можете добавить кучу различных методов в этом классе, которые нужны
    вам в работе с данными после их получения.
    It's useful class that helps to save a lot of code during validatio
    process in our tests. It receives response object and gets from it all
    values that should be validated. You can add additional methods into the
    Class if it needs for your project testing.
    """

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        """
        Метод для валидации статус кода. Из объекта респонса,
        который мы получили, мы берём статус и сравнимаем с тем, который
        нам был передан как параметр.
        Method for status code validation. It compares value from response
        object and compare it with received value from method params.
        """
        if isinstance(status_code, list):
            assert self.response_status in status_code
        else:
            assert self.response_status == status_code
        return self
