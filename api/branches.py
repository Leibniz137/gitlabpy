# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gitlabpy.verb import (
    DELETE,
    GET,
    POST,
    PUT
)
from .repositories import PATH as BASEPATH

PATH = BASEPATH + "/branches"


@GET
def list(**kwargs):
    """List repository branches"""
    return PATH.format(**kwargs), kwargs


SINGULAR = PATH + "/{branch}"

@GET
def single(**kwargs):
    """Get single repository branch"""
    return SINGULAR.format(**kwargs), kwargs


@PUT
def protect(**kwargs):
    """Protect repository branch"""
    return (SINGULAR + "/protect").format(**kwargs), kwargs


@PUT
def unprotect(**kwargs):
    """Unprotect repository branch"""
    return (SINGULAR + "/unprotect").format(**kwargs), kwargs


@POST
def create(**kwargs):
    """Create repository branch"""
    return PATH.format(**kwargs), kwargs


@DELETE
def delete(**kwargs):
    """Delete repository branch"""
    return SINGULAR.format(**kwargs), kwargs
