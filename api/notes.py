# -*- coding: utf-8 -*-

from ..http import (
    GET,
    POST,
    PUT
)

from .issues import PROJECT_ISSUE_PATH
from .projects import PATH as PROJECTS_PATH
from .merge_requests import SINGULAR as SINGULAR_MERGE_REQUEST


NOTES_PATH = PROJECT_ISSUE_PATH + "/notes"
SNIPPET_PATH = PROJECTS_PATH + "/notes"


@GET
def list(**kwargs):
    """List project issue notes"""
    return NOTES_PATH.format(**kwargs), kwargs


SINGULAR_NOTE = NOTES_PATH + "/{note_id}"


@GET
def single(**kwargs):
    """Get single issue note"""
    return NOTES_PATH.format(**kwargs), kwargs


@POST
def create(**kwargs):
    """Create new issue note"""
    return NOTES_PATH.format(**kwargs), kwargs


@PUT
def edit(**kwargs):
    """Modify existing issue note"""
    return SINGULAR_NOTE.format(**kwargs), kwargs


@GET
def list_snippets(**kwargs):
    """List all snippet notes"""
    return SNIPPET_PATH.format(**kwargs), kwargs


@GET
def single_snippet(**kwargs):
    """Get single snippet note"""
    return SINGULAR_NOTE.format(**kwargs), kwargs


@POST
def create_snippet(**kwargs):
    """Create new snippet note"""
    return SNIPPET_PATH.format(**kwargs), kwargs


@PUT
def edit_snippet(**kwargs):
    """Modify existing snippet note"""
    return SINGULAR_NOTE.format(**kwargs), kwargs


@GET
def list_merge_requests(**kwargs):
    """List all merge request notes"""
    return (SINGULAR_MERGE_REQUEST + "/notes").format(**kwargs), kwargs


@GET
def single_merge_request(**kwargs):
    """Get single merge request note"""
    return (SINGULAR_MERGE_REQUEST + "/notes/{note_id}").format(**kwargs), kwargs


@POST
def create_merge_request(**kwargs):
    """Create new merge request note"""
    return (SINGULAR_MERGE_REQUEST + "/notes").format(**kwargs), kwargs


@PUT
def edit_merge_request(**kwargs):
    """Modify existing merge request note"""
    return (SINGULAR_MERGE_REQUEST + "/notes/{note_id}").format(**kwargs), kwargs
