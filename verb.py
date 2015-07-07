# -*- coding: utf-8 -*-
import functools

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
        path, data = self.api_method(*args, **kwargs)
        request = functools.partial(
            getattr(self.urllib, self.__class__.__name__.lower()),
            data=data,
            headers=headers,
            verify=verify)

        response = request(host + path)
        responses = [response]

        if 'page' in kwargs:
            # so that page i isn't repeatedly requested. TODO: test this case
            del kwargs['page']
        while 'next' in response.links:
            response = request(response.links['next']['url'])
            responses.append(response)
        return responses


class GET(Verb):
    pass


class DELETE(Verb):
    pass


class POST(Verb):
    success = 201


class PUT(Verb):
    pass
