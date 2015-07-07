# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gitlabpy.verb import POST
from .base import PATH as BASEPATH


@POST
def login(**kwargs):
    return BASEPATH + "/session", kwargs

METHODS = [login]
