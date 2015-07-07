# -*- coding: utf-8 -*-

from ..verb import (
    DELETE,
    GET,
    POST
)

from .projects import SINGULAR as BASEPATH


PATH = BASEPATH + "/keys"


@GET
def list(**kwargs):
    """List deploy keys"""
    return PATH.format(**kwargs), kwargs

SINGULAR = PATH + "/{key_id}"


@GET
def single(**kwargs):
    """Single deploy key"""
    return SINGULAR.format(**kwargs), kwargs


@POST
def create(**kwargs):
    """Add deploy key"""
    return PATH.format(**kwargs), kwargs


@DELETE
def delete(**kwargs):
    """Delete deploy key"""
    return SINGULAR.format(**kwargs), kwargs
