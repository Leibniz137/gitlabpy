# -*- coding: utf-8 -*-

from ..http import (
    GET,
    POST,
    PUT
)
from .projects import PATH as BASEPATH


PATH = BASEPATH + "/milestones"


@GET
def list(**kwargs):
    """List project milestones"""
    return PATH, kwargs


SINGULAR = PATH + "/{milestone_id}"


@GET
def single(**kwargs):
    """Get single milestone"""
    return SINGULAR, kwargs


@POST
def create(**kwargs):
    """Create new milestone"""
    return PATH, kwargs


@PUT
def edit(**kwargs):
    """Edit milestone"""
    return SINGULAR, kwargs


@GET
def issues(**kwargs):
    """Get all issues assigned to a single milestone"""
    return SINGULAR + "/issues", kwargs
