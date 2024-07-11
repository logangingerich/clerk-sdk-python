"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel, Nullable
from clerk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateOrganizationPublicMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    
    

class UpdateOrganizationPublicMetadata(BaseModel):
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    
    

class UpdateOrganizationPrivateMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization that is only visible to your backend."""
    
    

class UpdateOrganizationPrivateMetadata(BaseModel):
    r"""Metadata saved on the organization that is only visible to your backend."""
    
    

class UpdateOrganizationRequestBodyTypedDict(TypedDict):
    public_metadata: NotRequired[UpdateOrganizationPublicMetadataTypedDict]
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    private_metadata: NotRequired[UpdateOrganizationPrivateMetadataTypedDict]
    r"""Metadata saved on the organization that is only visible to your backend."""
    name: NotRequired[Nullable[str]]
    r"""The new name of the organization"""
    slug: NotRequired[Nullable[str]]
    r"""The new slug of the organization, which needs to be unique in the instance"""
    max_allowed_memberships: NotRequired[Nullable[int]]
    r"""The maximum number of memberships allowed for this organization"""
    admin_delete_enabled: NotRequired[Nullable[bool]]
    r"""If true, an admin can delete this organization with the Frontend API."""
    

class UpdateOrganizationRequestBody(BaseModel):
    public_metadata: Optional[UpdateOrganizationPublicMetadata] = None
    r"""Metadata saved on the organization, that is visible to both your frontend and backend."""
    private_metadata: Optional[UpdateOrganizationPrivateMetadata] = None
    r"""Metadata saved on the organization that is only visible to your backend."""
    name: Optional[Nullable[str]] = None
    r"""The new name of the organization"""
    slug: Optional[Nullable[str]] = None
    r"""The new slug of the organization, which needs to be unique in the instance"""
    max_allowed_memberships: Optional[Nullable[int]] = None
    r"""The maximum number of memberships allowed for this organization"""
    admin_delete_enabled: Optional[Nullable[bool]] = None
    r"""If true, an admin can delete this organization with the Frontend API."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["public_metadata", "private_metadata", "name", "slug", "max_allowed_memberships", "admin_delete_enabled"]
        nullable_fields = ["name", "slug", "max_allowed_memberships", "admin_delete_enabled"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        

class UpdateOrganizationRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization to update"""
    request_body: UpdateOrganizationRequestBodyTypedDict
    

class UpdateOrganizationRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the organization to update"""
    request_body: Annotated[UpdateOrganizationRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
