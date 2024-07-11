"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel
from clerk.utils import FieldMetadata, PathParamMetadata
from enum import Enum
from typing import TypedDict
from typing_extensions import Annotated


class PathParamTemplateType(str, Enum):
    r"""The type of templates to retrieve (email or SMS)"""
    EMAIL = "email"
    SMS = "sms"


class GetTemplateRequestTypedDict(TypedDict):
    template_type: PathParamTemplateType
    r"""The type of templates to retrieve (email or SMS)"""
    slug: str
    r"""The slug (i.e. machine-friendly name) of the template to retrieve"""
    

class GetTemplateRequest(BaseModel):
    template_type: Annotated[PathParamTemplateType, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The type of templates to retrieve (email or SMS)"""
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The slug (i.e. machine-friendly name) of the template to retrieve"""
    
