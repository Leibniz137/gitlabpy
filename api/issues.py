# -*- coding: utf-8 -*-

from ..http import (
    GET,
    PUT
)
from .projects import PATH as PROJECTPATH
from .base import PATH as BASEPATH

PATH = BASEPATH + "/issues"
PROJECT_ISSUES_PATH = PROJECTPATH + "/issues"
PROJECT_ISSUE_PATH = PROJECT_ISSUES_PATH + "/{issue_id}"


@GET
def list(**kwargs):
    """List issues"""
    return PATH, kwargs


@GET
def project(**kwargs):
    """List project issues"""
    return PROJECT_ISSUES_PATH.format(**kwargs), kwargs


@GET
def single(**kwargs):
    """Single issue"""
    return PROJECT_ISSUE_PATH.format(**kwargs), kwargs


@GET
def create(**kwargs):
    """New issue"""
    return PROJECT_ISSUES_PATH.format(**kwargs), kwargs


@PUT
def edit(**kwargs):
    """Edit issue"""
    return PROJECT_ISSUE_PATH.format(**kwargs), kwargs
