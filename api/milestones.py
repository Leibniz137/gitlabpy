# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gitlabpy.verb import (
    GET,
    POST,
    PUT
)
from .projects import PATH as BASEPATH


PATH = BASEPATH + "/milestones"


@GET
def list(**kwargs):
    """List project milestones"""
    return PATH.format(**kwargs), kwargs


SINGULAR = PATH + "/{milestone_id}"


@GET
def single(**kwargs):
    """Get single milestone"""
    return SINGULAR.format(**kwargs), kwargs


@POST
def create(**kwargs):
    """Create new milestone"""
    return PATH.format(**kwargs), kwargs


@PUT
def edit(**kwargs):
    """Edit milestone"""
    return SINGULAR.format(**kwargs), kwargs


@GET
def issues(**kwargs):
    """Get all issues assigned to a single milestone"""
    return (SINGULAR + "/issues").format(**kwargs), kwargs
