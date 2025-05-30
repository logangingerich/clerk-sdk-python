"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteDomainRequestTypedDict(TypedDict):
    domain_id: str
    r"""The ID of the domain that will be deleted. Must be a satellite domain."""


class DeleteDomainRequest(BaseModel):
    domain_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the domain that will be deleted. Must be a satellite domain."""
