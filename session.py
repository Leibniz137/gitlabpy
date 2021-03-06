# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    unicode_literals
)
from builtins import object
from functools import partial

from . import api

from .credentials import Token


class SessionError(Exception):
    def __init__(self, string, response):
        super(SessionError, self).__init__(string)
        self.response = response


class Session(object):
    """
    Session instances are the primary means by which users can interact with
    the Gitlab api

    by default, session instances enforce SSL verification
    """
    verify = True

    @classmethod
    def from_login(cls, baseurl, verify=verify, **kwargs):
        """
        kwargs should include
        either 'login' or 'email' keys, as well as a 'password' key
        """
        headers = {'connection': 'close'}
        (response,) = api.session.login(baseurl, headers, verify, **kwargs)
        if response.status_code == api.session.login.success:
            token = Token(response.json()['private_token'])
        else:
            raise SessionError(
                "Failed to login: {0.reason}".format(response), response)
        return cls(baseurl, token, verify)

    def __init__(self, baseurl, token, verify=verify):
        headers = {token.key: token.value}

        class Resource(object):
            def __init__(self, methods):
                for method in methods:
                    setattr(
                        self,
                        method.__name__,
                        partial(method, baseurl, headers, verify)
                    )
        self.resource_cls = Resource

    def __getattr__(self, name):
        """
        __getattr__ is the mechanism for populating Session instance with
        api Resources, (whose connection details are specific to the instance).

        __getattr__ first attempts normal lookup (via parent's __getattr__).
        If attribute doesn't exist, loads api resource
        """
        try:
            return super(Session, self).__getattr__(name)
        except AttributeError:
            api_resource = getattr(api, name)
            resource = self.resource_cls(api_resource.METHODS)
            setattr(self, name, resource)
            return resource
