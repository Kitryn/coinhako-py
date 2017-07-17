import requests
from .api_map import _API_MAP

BASE_URL = 'https://www.coinhako.com/api/v1'


class Coinhako(object):
    def __init__(self, api_map=_API_MAP):
        self.api_map = api_map

    def __getattr__(self, item):
        """

        :param item: Key inside api_map
        :return:
        """
        instance = Coinhako(self.api_map[item])
        setattr(self, item, instance)
        return instance

    def __call__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        url = self.api_map['url']
        full_url = BASE_URL + url
        method = self.api_map['method']
        return requests.request(method, full_url).json()  # TODO: Handle params and errors
