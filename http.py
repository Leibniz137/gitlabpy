# -*- coding: utf-8 -*-
import requests


class Verb(object):
    success = 200  # return code
    urllib = requests

    def __init__(self, fn):
        self.api_method = fn
        self.__name__ = fn.__name__
        self.__doc__ = fn.__doc__

    def __call__(self, host, headers, verify, *args, **kwargs):
        """
        decorates api_method, returns a function that can be passed to session
        """
        request = getattr(self.urllib, self.__class__.__name__.lower())

        path, data = self.api_method(*args, **kwargs)
        return request(host + path, data=data, headers=headers, verify=verify)


class GET(Verb):
    pass


class DELETE(Verb):
    pass


class POST(Verb):
    success = 201
    pass


class PUT(Verb):
    pass
