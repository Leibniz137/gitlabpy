# -*- coding: utf-8 -*-

from ..verb import (
    GET,
    POST
)
from .projects import PATH as BASEPATH

PATH = BASEPATH + "/repository"

TAGS_PATH = PATH + "/tags"


@GET
def list_tags(**kwargs):
    """List project repository tags"""
    return TAGS_PATH.format(**kwargs), kwargs


@POST
def create_tag(**kwargs):
    """Create a new tag"""
    return TAGS_PATH.format(**kwargs), kwargs


@GET
def list_tree(**kwargs):
    """List repository tree"""
    return (PATH + "/tree").format(**kwargs), kwargs


@GET
def raw_file(**kwargs):
    """Raw file content"""
    return (PATH + "/blobs/{sha}").format(**kwargs), kwargs


@GET
def raw_blob(**kwargs):
    """Raw blob content"""
    return (PATH + "/raw_blobs/{sha}").format(**kwargs), kwargs


@GET
def file_archive(**kwargs):
    """Get file archive"""
    return (PATH + "/archive").format(**kwargs), kwargs


@GET
def compare(**kwargs):
    """Compare branches, tags or commits"""
    return (PATH + "/compare").format(**kwargs), kwargs


@GET
def contributors(**kwargs):
    """Contributors"""
    return (PATH + "/contributors").format(**kwargs), kwargs

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
