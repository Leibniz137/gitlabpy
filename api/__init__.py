# -*- coding: utf-8 -*-

RESOURCES = ["groups", "session"]

for resource in RESOURCES:
    exec("from {} import *".format(resource))
