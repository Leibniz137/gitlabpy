# -*- coding: utf-8 -*-
from ..http import (
    DELETE,
    GET,
    POST,
    PUT
)
from .base import PATH as BASEPATH

SINGULAR = BASEPATH + "/user"
PLURAL = SINGULAR + "s"


@GET
def list(**kwargs):
    """List users"""
    return PLURAL, kwargs


@GET
def single(**kwargs):
    """Single user"""
    return (PLURAL + "/{id}").format(**kwargs), kwargs


@POST
def create(**kwargs):
    """User creation"""
    return PLURAL, kwargs


@PUT
def modify(**kwargs):
    """User modification"""
    return (PLURAL + "/{id}").format(**kwargs), kwargs


@DELETE
def delete(**kwargs):
    """User deletion"""
    return (PLURAL + "/{id}").format(**kwargs), kwargs


@GET
def current(**kwargs):
    """Current user"""
    return SINGULAR, kwargs


@GET
def current_keys(**kwargs):
    """List SSH keys"""
    return SINGULAR + "/keys", kwargs


@GET
def keys(**kwargs):
    """List SSH keys for user"""
    return (PLURAL + "/{uid}/keys").format(**kwargs), kwargs


@GET
def key(**kwargs):
    """Single SSH Key"""
    return (SINGULAR + "/keys/{id}").format(**kwargs), kwargs


@POST
def add_key(**kwargs):
    """Add SSH key"""
    return SINGULAR + "/keys", kwargs


@POST
def add_user_key(**kwargs):
    """Add SSH key for user"""
    return (PLURAL + "/{id}/keys").format(**kwargs), kwargs


@DELETE
def delete_key(**kwargs):
    """Delete SSH key for current user"""
    return (SINGULAR + "/keys/{id}").format(**kwargs), kwargs


@DELETE
def delete_user_key(**kwargs):
    """Delete SSH key for a given user"""
    return (PLURAL + "/{uid}/keys/{id}").format(**kwargs), kwargs

METHODS = [
    add_key,
    add_user_key,
    create,
    current,
    current_keys,
    delete,
    delete_key,
    delete_user_key,
    key,
    keys,
    list,
    modify,
    single
]
