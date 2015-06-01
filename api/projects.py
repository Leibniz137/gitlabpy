# -*- coding: utf-8 -*-

from ..http import (
    DELETE,
    GET,
    POST,
    PUT
)
from .base import PATH as BASEPATH

PATH = BASEPATH + "/projects"
SINGULAR = PATH + "/{id}"


@GET
def list(**kwargs):
    """List projects"""
    return PATH, kwargs


@GET
def owned(**kwargs):
    """List owned projects"""
    return PATH + "/owned", kwargs


@GET
def all(**kwargs):
    """List ALL projects"""
    return PATH + "/all", kwargs


@GET
def single(**kwargs):
    """Get single project"""
    return SINGULAR.format(**kwargs), kwargs


@GET
def events(**kwargs):
    """Get project events"""
    return SINGULAR + "/events", kwargs


@POST
def create(**kwargs):
    """Create project"""
    return PATH, kwargs


@POST
def create_for_user(**kwargs):
    """Create project for user"""
    return PATH + "/user/{user_id}".format(**kwargs), kwargs


@PUT
def edit(**kwargs):
    """Edit project"""
    return SINGULAR.format(**kwargs), kwargs


@POST
def fork(**kwargs):
    """Fork project"""
    return PATH + "/fork/{id}".format(**kwargs), kwargs


@DELETE
def remove(**kwargs):
    """Remove project"""
    return SINGULAR.format(**kwargs), kwargs


MEMBERS_PATH = SINGULAR + "/members"
MEMBER_PATH = MEMBERS_PATH + "/{user_id}"


@GET
def members(**kwargs):
    """List project team members"""
    return MEMBERS_PATH.format(**kwargs), kwargs


@GET
def member(**kwargs):
    """Get project team member"""
    return MEMBER_PATH.format(**kwargs), kwargs


@POST
def add_member(**kwargs):
    """Add project team member"""
    return MEMBERS_PATH.format(**kwargs), kwargs


@PUT
def edit_member(**kwargs):
    """Edit project team member"""
    return MEMBER_PATH.format(**kwargs), kwargs


@DELETE
def remove_member(**kwargs):
    """Remove project team member"""
    return MEMBER_PATH.format(**kwargs), kwargs


HOOKS_PATH = SINGULAR + "/hooks"
HOOK_PATH = HOOKS_PATH + "/{hook_id}"


@GET
def hooks(**kwargs):
    """List project hooks"""
    return HOOKS_PATH.format(**kwargs), kwargs


@GET
def hook(**kwargs):
    """Get project hook"""
    return HOOK_PATH.format(**kwargs), kwargs


@POST
def add_hook(**kwargs):
    """Add project hook"""
    return HOOKS_PATH.format(**kwargs), kwargs


@PUT
def edit_hook(**kwargs):
    """Edit project hook"""
    return HOOK_PATH.format(**kwargs), kwargs


@DELETE
def delete_hook(**kwargs):
    """Delete project hook"""
    return HOOK_PATH.format(**kwargs), kwargs


BRANCHES_PATH = SINGULAR + "/repository"
BRANCH_PATH = BRANCHES_PATH + "/{branch}"


@GET
def branches(**kwargs):
    """List branches"""
    return BRANCHES_PATH.format(**kwargs), kwargs


@GET
def branch(**kwargs):
    """List single branch"""
    return BRANCH_PATH.format(**kwargs), kwargs


@PUT
def protect(**kwargs):
    """Protect single branch"""
    return (BRANCH_PATH + "/protect").format(**kwargs), kwargs


@PUT
def unprotect(**kwargs):
    """Unprotect single branch"""
    return (BRANCH_PATH + "/unprotect").format(**kwargs), kwargs


FORK_PATH = SINGULAR + "/fork"


@POST
def forked(**kwargs):
    """Create a forked from/to relation between existing projects"""
    return FORK_PATH + "/{forked_from_id}".format(**kwargs), kwargs


@DELETE
def unforked(**kwargs):
    """Delete an existing forked from relationship"""
    return FORK_PATH.format(**kwargs), kwargs


@GET
def search(**kwargs):
    return PATH + "/search/{query}".format(**kwargs), kwargs


METHODS = [
    all,
    add_hook,
    add_member,
    branch,
    branches,
    create,
    create_for_user,
    delete_hook,
    edit,
    edit_hook,
    edit_member,
    events,
    fork,
    forked,
    hook,
    hooks,
    list,
    member,
    members,
    owned,
    protect,
    remove,
    remove_member,
    search,
    single,
    unforked,
    unprotect,
]
