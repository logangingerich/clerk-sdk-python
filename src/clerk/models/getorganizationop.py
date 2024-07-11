"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel
from clerk.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class GetOrganizationRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID or slug of the organization"""
    

class GetOrganizationRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID or slug of the organization"""
    
