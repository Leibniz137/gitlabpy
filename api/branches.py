# -*- coding: utf-8 -*-

from ..http import (
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
    return PATH, kwargs


SINGULAR = PATH + "/{branch}"

@GET
def single(**kwargs):
    """Get single repository branch"""
    return SINGULAR, kwargs


@PUT
def protect(**kwargs):
    """Protect repository branch"""
    return SINGULAR + "/protect", kwargs


@PUT
def unprotect(**kwargs):
    """Unprotect repository branch"""
    return SINGULAR + "/unprotect", kwargs


@POST
def create(**kwargs):
    """Create repository branch"""
    return PATH, kwargs


@DELETE
def delete(**kwargs):
    """Delete repository branch"""
    return SINGULAR, kwargs
