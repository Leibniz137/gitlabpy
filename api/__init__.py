# -*- coding: utf-8 -*-
# import os

# BASE_PATH = "/api/v3"
RESOURCES = ["groups", "projects", "session", "users"]

for resource in RESOURCES:
    exec("import {}".format(resource))
