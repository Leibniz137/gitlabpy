# -*- coding: utf-8 -*-

from ..http import (
    DELETE,
    GET,
    POST,
    PUT
)

from .projects import PATH as BASEPATH


PATH = BASEPATH + "/labels"


@GET
def list(**kwargs):
    """List labels"""
    return PATH, kwargs


@POST
def create(**kwargs):
    """Create a new label"""
    return PATH, kwargs


@DELETE
def delete(**kwargs):
    """Delete a label"""
    return PATH, kwargs


@PUT
def edit(**kwargs):
    """Edit an existing label"""
    return PATH, kwargs
