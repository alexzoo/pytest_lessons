import requests


class Request:

    def __init__(self, url):
        self.url = url

    def get(self, params):
        """
        Get request
        """
        return requests.get(url=self.url, params=params)

    def post(self, data):
        pass

    def delete(self, data):
        pass

