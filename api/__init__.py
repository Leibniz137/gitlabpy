# -*- coding: utf-8 -*-

RESOURCES = ["Groups", "Session"]

for resource in RESOURCES:
    exec("from {} import *".format(resource))
