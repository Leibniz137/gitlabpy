# -*- coding: utf-8 -*-
"""
module for representing gitlab api tokens
"""


class Token(object):
    key = "PRIVATE-TOKEN"

    def __init__(self, value):
        self.value = value


class OAuth(Token):
    key = "Authorization"

    def __init__(self, value):
        self.value = 'Bearer {}'.format(value)
