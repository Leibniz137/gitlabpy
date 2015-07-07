# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gitlabpy.verb import (
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
    return PATH.format(**kwargs), kwargs


@GET
def single(**kwargs):
    """Single snippet"""
    return SINGULAR.format(**kwargs), kwargs


@POST
def create(**kwargs):
    """Create new snippet"""
    return PATH.format(**kwargs), kwargs


@PUT
def update(**kwargs):
    """Update snippet"""
    return SINGULAR.format(**kwargs), kwargs


@DELETE
def delete(**kwargs):
    """Delete snippet"""
    return SINGULAR.format(**kwargs), kwargs


@GET
def content(**kwargs):
    """Snippet content"""
    return (SINGULAR + "/raw").format(**kwargs), kwargs

METHODS = [
    content,
    create,
    delete,
    list,
    single,
    update
]
