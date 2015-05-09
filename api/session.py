# -*- coding: utf-8 -*-

from ..http import POST
from .base import PATH as BASEPATH


@POST
def login(**kwargs):
    return BASEPATH + "/session", kwargs

METHODS = [login]
