# -*- coding: utf-8 -*-

from ..http import (
    GET,
    POST,
    PUT
)

from .projects import PATH as BASEPATH

PATH = BASEPATH + "/merge_requests"


@GET
def list(**kwargs):
    """List merge requests"""
    return PATH, kwargs

SINGULAR = PATH + "{merge_request_id}"


@GET
def single(**kwargs):
    """Get single MR"""
    return SINGULAR, kwargs


@GET
def single_changes(**kwargs):
    """Get single MR changes"""
    return SINGULAR + "/changes", kwargs


@POST
def create(**kwargs):
    """Create MR"""
    return PATH, kwargs


@PUT
def update(**kwargs):
    """Update MR"""
    return SINGULAR, kwargs


@PUT
def accept(**kwargs):
    """Accept MR"""
    return SINGULAR + "/merge", kwargs


@POST
def comment(**kwargs):
    """Post comment to MR"""
    return SINGULAR + "/comments", kwargs


@GET
def comments(**kwargs):
    """Get the comments on a MR"""
    return SINGULAR + "/comments", kwargs
