# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gitlabpy.verb import (
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
    return PATH.format(**kwargs), kwargs


@POST
def create(**kwargs):
    """Create a new label"""
    return PATH.format(**kwargs), kwargs


@DELETE
def delete(**kwargs):
    """Delete a label"""
    return PATH.format(**kwargs), kwargs


@PUT
def edit(**kwargs):
    """Edit an existing label"""
    return PATH.format(**kwargs), kwargs
