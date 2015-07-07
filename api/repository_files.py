# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gitlabpy.verb import (
    DELETE,
    GET,
    POST,
    PUT
)
from .repositories import PATH as BASEPATH

PATH = BASEPATH + "/files"


@GET
def single(**kwargs):
    """Get file from repository"""
    return PATH.format(**kwargs), kwargs


@POST
def new(**kwargs):
    """Create new file in repository"""
    return PATH.format(**kwargs), kwargs


@PUT
def update(**kwargs):
    """Update existing file in repository"""
    return PATH.format(**kwargs), kwargs


@DELETE
def delete(**kwargs):
    """Delete existing file in repository"""
    return PATH.format(**kwargs), kwargs
