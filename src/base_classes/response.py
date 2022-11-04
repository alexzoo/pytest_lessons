# from jsonschema import validate


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
        self.response_json = response.json()
        # self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        """
        Method for status code validation. It compares value from response
        object and compare it with received value from method params.
        """
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return \
            f'\nStatus code: {self.response_status} \n' \
            f'Requested url: {self.response.url} \n' \
            f'Response body: {self.response_json}'
