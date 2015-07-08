# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    unicode_literals
)

RESOURCES = [
    "branches",
    "commits",
    "deploy_keys",
    "groups",
    "issues",
    "labels",
    "merge_requests",
    "milestones",
    "notes",
    "project_snippets",
    "projects",
    "repositories",
    "repository_files",
    "services",
    "session",
    "users"
]

for resource in RESOURCES:
    exec("from . import {0}".format(resource))
