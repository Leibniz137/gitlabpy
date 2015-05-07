# -*- coding: utf-8 -*-

from ..http import POST
from .base import PATH as BASEPATH


@POST
def Login(**kwargs):
    return BASEPATH + "/session", kwargs

METHODS = [Login]
