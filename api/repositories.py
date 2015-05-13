# -*- coding: utf-8 -*-

from ..http import (
    DELETE,
    GET,
    POST,
    PUT
)
from .projects import PATH as BASEPATH

PATH = BASEPATH + "/repository"

TAGS_PATH = PATH + "/tags"


@GET
def list_tags(**kwargs):
    """List project repository tags"""
    return TAGS_PATH, kwargs


@POST
def create_tag(**kwargs):
    """Create a new tag"""
    return TAGS_PATH, kwargs


@GET
def list_tree(**kwargs):
    """List repository tree"""
    return PATH + "/tree", kwargs


@GET
def raw_file(**kwargs):
    """Raw file content"""
    return PATH + "/blobs/{sha}", kwargs


@GET
def raw_blob(**kwargs):
    """Raw blob content"""
    return PATH + "/raw_blobs/{sha}", kwargs


@GET
def file_archive(**kwargs):
    """Get file archive"""
    return PATH + "/archive", kwargs


@GET
def compare(**kwargs):
    """Compare branches, tags or commits"""
    return PATH + "/compare", kwargs


@GET
def contributors(**kwargs):
    """Contributors"""
    return PATH + "/contributors", kwargs

METHODS = [
    compare,
    contributors,
    create_tag,
    file_archive,
    list_tags,
    list_tree,
    raw_blob,
    raw_file
]
