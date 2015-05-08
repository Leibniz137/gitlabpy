# -*- coding: utf-8 -*-
from functools import partial

import api
from credentials import (
    OAuth,
    Token,
)


class SessionError(Exception):
    def __init__(self, string, response):
        super(SessionError, self).__init__(string)
        self.response = response


class Session(object):
    @classmethod
    def from_login(cls, host, verify=True, **kwargs):
        """
        kwargs should include
        either 'login' or 'email' keys, as well as a 'password' key
        """
        headers = {'connection': 'close'}
        response = api.session.login(host, headers, verify, **kwargs)
        if response.status_code == api.session.login.success:
            token = Token(response.json()['private_token'])
        else:
            raise SessionError(
                "Failed to login: {}".format(response.reason), response)
        return cls(host, token, verify)

    def __init__(self, host, token, verify=True):
        headers = {token.key: token.value}

        class Resource(object):
            def __init__(self, methods):
                for method in methods:
                    setattr(
                        self,
                        method.__name__,
                        partial(method, host, headers, verify)
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
