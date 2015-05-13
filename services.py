# -*- coding: utf-8 -*-

from ..http import (
    DELETE,
    PUT
)
from .projects import PATH as BASEPATH


PATH = BASEPATH + "/{id}/services"
CI_PATH = PATH + "/gitlab-ci"
HIPCHAT_PATH = PATH + "/hipchat"


@PUT
def edit_gitlabci(**kwargs):
    """Edit GitLab CI service"""
    return CI_PATH, kwargs


@DELETE
def delete_gitlabci(**kwargs):
    """Delete GitLab CI service"""
    return CI_PATH, kwargs


@PUT
def edit_hipchat(**kwargs):
    """Edit HipChat service"""
    return HIPCHAT_PATH, kwargs


@DELETE
def delete_hipchat(**kwargs):
    """Delete HipChat service"""
    return HIPCHAT_PATH, kwargs
