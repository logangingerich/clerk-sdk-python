"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel, Nullable
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateInstanceRequestBodyTypedDict(TypedDict):
    test_mode: NotRequired[Nullable[bool]]
    r"""Toggles test mode for this instance, allowing the use of test email addresses and phone numbers.
    Defaults to true for development instances.
    """
    hibp: NotRequired[Nullable[bool]]
    r"""Whether the instance should be using the HIBP service to check passwords for breaches"""
    enhanced_email_deliverability: NotRequired[Nullable[bool]]
    r"""The \"enhanced_email_deliverability\" feature will send emails from \"verifications@clerk.dev\" instead of your domain.
    This can be helpful if you do not have a high domain reputation.
    """
    support_email: NotRequired[Nullable[str]]
    clerk_js_version: NotRequired[Nullable[str]]
    development_origin: NotRequired[Nullable[str]]
    allowed_origins: NotRequired[List[str]]
    r"""For browser-like stacks such as browser extensions, Electron, or Capacitor.js the instance allowed origins need to be updated with the request origin value.
    For Chrome extensions popup, background, or service worker pages the origin is chrome-extension://extension_uiid. For Electron apps the default origin is http://localhost:3000. For Capacitor, the origin is capacitor://localhost.
    """
    cookieless_dev: NotRequired[bool]
    r"""Whether the instance should operate in cookieless development mode (i.e. without third-party cookies).
    Deprecated: Please use `url_based_session_syncing` instead.
    """
    url_based_session_syncing: NotRequired[bool]
    r"""Whether the instance should use URL-based session syncing in development mode (i.e. without third-party cookies)."""
    

class UpdateInstanceRequestBody(BaseModel):
    test_mode: Optional[Nullable[bool]] = None
    r"""Toggles test mode for this instance, allowing the use of test email addresses and phone numbers.
    Defaults to true for development instances.
    """
    hibp: Optional[Nullable[bool]] = None
    r"""Whether the instance should be using the HIBP service to check passwords for breaches"""
    enhanced_email_deliverability: Optional[Nullable[bool]] = None
    r"""The \"enhanced_email_deliverability\" feature will send emails from \"verifications@clerk.dev\" instead of your domain.
    This can be helpful if you do not have a high domain reputation.
    """
    support_email: Optional[Nullable[str]] = None
    clerk_js_version: Optional[Nullable[str]] = None
    development_origin: Optional[Nullable[str]] = None
    allowed_origins: Optional[List[str]] = None
    r"""For browser-like stacks such as browser extensions, Electron, or Capacitor.js the instance allowed origins need to be updated with the request origin value.
    For Chrome extensions popup, background, or service worker pages the origin is chrome-extension://extension_uiid. For Electron apps the default origin is http://localhost:3000. For Capacitor, the origin is capacitor://localhost.
    """
    cookieless_dev: Annotated[Optional[bool], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.")] = None
    r"""Whether the instance should operate in cookieless development mode (i.e. without third-party cookies).
    Deprecated: Please use `url_based_session_syncing` instead.
    """
    url_based_session_syncing: Optional[bool] = None
    r"""Whether the instance should use URL-based session syncing in development mode (i.e. without third-party cookies)."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["test_mode", "hibp", "enhanced_email_deliverability", "support_email", "clerk_js_version", "development_origin", "allowed_origins", "cookieless_dev", "url_based_session_syncing"]
        nullable_fields = ["test_mode", "hibp", "enhanced_email_deliverability", "support_email", "clerk_js_version", "development_origin"]
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
        
