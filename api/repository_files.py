# -*- coding: utf-8 -*-

from ..http import (
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
    return PATH, kwargs


@POST
def new(**kwargs):
    """Create new file in repository"""
    return PATH, kwargs


@PUT
def update(**kwargs):
    """Update existing file in repository"""
    return PATH, kwargs


@DELETE
def delete(**kwargs):
    """Delete existing file in repository"""
    return PATH, kwargs