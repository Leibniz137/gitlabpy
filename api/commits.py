# -*- coding: utf-8 -*-

from ..http import (
    GET,
    POST,
)
from .repositories import PATH as BASEPATH

PATH = BASEPATH + "/commits"


@GET
def list(**kwargs):
    """List repository commits"""
    return PATH, kwargs


SHA_PATH = PATH + "/{sha}"


@GET
def single(**kwargs):
    """Get a single commit"""
    return SHA_PATH, kwargs


@GET
def diff(**kwargs):
    """Get the diff of a commit"""
    return SHA_PATH + "/diff", kwargs


COMMENTS_PATH = SHA_PATH + "/comments"


@GET
def comments(**kwargs):
    """Get the comments of a commit"""
    return COMMENTS_PATH, kwargs


@POST
def comment(**kwargs):
    """Post comment to commit"""
    return COMMENTS_PATH, kwargs
