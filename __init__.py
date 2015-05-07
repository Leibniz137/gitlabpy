# -*- coding: utf-8 -*-
from functools import partial

import api
from credentials import (
    OAuth,
    Token,
)


class Session(object):
    def __init__(self, host, token, verify):
        headers = {token.key: token.value}

        class Resource(object):
            def __init__(self, methods):
                for method in methods:
                    setattr(
                        self,
                        method.__name__,
                        partial(method, host, token, headers, verify)
                    )
        self.resource_cls = Resource

    def __getattr__(self, name):
        try:
            return super(Session, self).__getattr__(name)
        except AttributeError:
            api_resource = getattr(api, name)
            resource = self.resource_cls(api_resource.METHODS)
            setattr(self, name, resource)
            return resource


__all__ = ["Session", "Token", "OAuth"]
