from pydantic import ValidationError


class Response:

    """
    It's useful class that helps to save a lot of code during validation
    process in our tests. It receives response object and gets from it all
    values that should be validated. You can add additional methods into the
    Class if it needs for your project testing.
    """

    def __init__(self, response):
        self.parsed_object = None
        self.response = response
        self.json = response.json()
        self.status = response.status_code

    def validate(self, schema):
        try:
            if isinstance(self.json, list):
                for item in self.json:
                    parsed_object = schema.parse_obj(item)
                    self.parsed_object = parsed_object
            else:
                schema.parse_obj(self.json)
        except ValidationError:
            raise AssertionError(
                'Could not map received object to pydantic schema'
            )

    def assert_status_code(self, status_code):
        """
        Method for status code validation. It compares value from response
        object and compare it with received value from method params.
        """
        if isinstance(status_code, list):
            assert self.status in status_code, self
        else:
            assert self.status == status_code, self
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return \
            f'\nStatus code: {self.status} \n' \
            f'Requested url: {self.response.url} \n' \
            f'Response body: {self.json}'
