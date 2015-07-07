# -*- coding: utf-8 -*-

from ..verb import (
    GET,
    POST,
    PUT
)

from .projects import PATH as BASEPATH

PATH = BASEPATH + "/merge_requests"


@GET
def list(**kwargs):
    """List merge requests"""
    return PATH.format(**kwargs), kwargs

SINGULAR = PATH + "{merge_request_id}"


@GET
def single(**kwargs):
    """Get single MR"""
    return SINGULAR.format(**kwargs), kwargs


@GET
def single_changes(**kwargs):
    """Get single MR changes"""
    return (SINGULAR + "/changes").format(**kwargs), kwargs


@POST
def create(**kwargs):
    """Create MR"""
    return PATH.format(**kwargs), kwargs


@PUT
def update(**kwargs):
    """Update MR"""
    return SINGULAR.format(**kwargs), kwargs


@PUT
def accept(**kwargs):
    """Accept MR"""
    return (SINGULAR + "/merge").format(**kwargs), kwargs


@POST
def comment(**kwargs):
    """Post comment to MR"""
    return (SINGULAR + "/comments").format(**kwargs), kwargs


@GET
def comments(**kwargs):
    """Get the comments on a MR"""
    return (SINGULAR + "/comments").format(**kwargs), kwargs
