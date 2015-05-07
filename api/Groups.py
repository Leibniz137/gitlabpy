# -*- coding: utf-8 -*-
from ..http import (
    DELETE,
    GET,
    POST,
)
from .base import PATH as BASEPATH

PATH = BASEPATH + "/groups"


@GET
def All(**kwargs):
    return PATH, kwargs


@GET
def Details(**kwargs):
    return PATH + "/{id}".format(**kwargs), kwargs


@POST
def New(**kwargs):
    return PATH, kwargs


@POST
def Transfer(**kwargs):
    return PATH + "/{id}/projects/{project_id}".format(**kwargs), kwargs


@DELETE
def Remove(**kwargs):
    return PATH + "/{id}".format(**kwargs), kwargs


# @GET
# def Search(**kwargs):
#     return PATH +

METHODS = [All, Details, New, Transfer, Remove]
