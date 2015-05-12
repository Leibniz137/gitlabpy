# -*- coding: utf-8 -*-

from ..http import (
    DELETE,
    GET,
    POST,
    PUT
)
from .projects import PATH as BASEPATH

PATH = BASEPATH + "/{id}/snippets"
SINGULAR = PATH + "/{snippet_id}"


@GET
def list(**kwargs):
    """List snippets"""
    return PATH, kwargs


@GET
def single(**kwargs):
    """Single snippet"""
    return SINGULAR, kwargs


@POST
def create(**kwargs):
    """Create new snippet"""
    return PATH, kwargs


@PUT
def update(**kwargs):
    """Update snippet"""
    return SINGULAR, kwargs


@DELETE
def delete(**kwargs):
    """Delete snippet"""
    return SINGULAR, kwargs


@GET
def content(**kwargs):
    """Snippet content"""
    return SINGULAR + "/raw", kwargs

METHODS = [
    content,
    create,
    delete,
    list,
    single,
    update
]
