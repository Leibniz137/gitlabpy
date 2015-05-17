# -*- coding: utf-8 -*-

from ..http import (
    DELETE,
    GET,
    POST
)

from .projects import SINGULAR as BASEPATH


PATH = BASEPATH + "/keys"


@GET
def list(**kwargs):
    """List deploy keys"""
    return PATH, kwargs

SINGULAR = PATH + "/{key_id}"


@GET
def single(**kwargs):
    """Single deploy key"""
    return SINGULAR, kwargs


@POST
def create(**kwargs):
    """Add deploy key"""
    return PATH, kwargs


@DELETE
def delete(**kwargs):
    """Delete deploy key"""
    return SINGULAR, kwargs
