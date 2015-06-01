# -*- coding: utf-8 -*-
# import os

# BASE_PATH = "/api/v3"
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
    exec("import {}".format(resource))
