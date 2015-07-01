# -*- coding: utf-8 -*-
from ..http import (
    DELETE,
    GET,
    POST,
    PUT
)
from .base import PATH as BASEPATH

PATH = BASEPATH + "/groups"


@GET
def list(**kwargs):
    """List project groups"""
    return PATH, kwargs


@GET
def details(**kwargs):
    """Details of a group"""
    return (PATH + "/{id}").format(**kwargs), kwargs


@POST
def new(**kwargs):
    """New group"""
    return PATH, kwargs


@POST
def transfer(**kwargs):
    """Transfer project to group"""
    return (PATH + "/{id}/projects/{project_id}").format(**kwargs), kwargs


@DELETE
def remove(**kwargs):
    """Remove group"""
    return (PATH + "/{id}").format(**kwargs), kwargs


@GET
def search(*args):   # TODO: should this be changed to kwargs???
    """Search for a group"""
    return (PATH + "?search={0}").format(*args), {}


@GET
def members(**kwargs):
    """List group members"""
    return (PATH + "/{id}/members").format(**kwargs), kwargs


@POST
def add_member(**kwargs):
    """Add group member"""
    return (PATH + "/{id}/members").format(**kwargs), kwargs


@PUT
def edit_member(**kwargs):
    """Edit group team member"""
    return (PATH + "/{id}/members/{user_id}").format(**kwargs), kwargs


@DELETE
def remove_member(**kwargs):
    return (PATH + "/{id}/members/{user_id}").format(**kwargs), kwargs


METHODS = [
    add_member,
    details,
    edit_member,
    list,
    members,
    new,
    transfer,
    remove,
    remove_member,
    search
]
