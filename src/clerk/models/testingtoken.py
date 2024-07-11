"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel
from enum import Enum
from typing import TypedDict


class TestingTokenObject(str, Enum):
    TESTING_TOKEN = "testing_token"


class TestingTokenTypedDict(TypedDict):
    __test__ = False
    
    object: TestingTokenObject
    token: str
    r"""The actual token. This value is meant to be passed in the `__clerk_testing_token` query parameter with requests to the Frontend API."""
    expires_at: int
    r"""Unix timestamp of the token's expiration time.

    """
    

class TestingToken(BaseModel):
    __test__ = False
    
    object: TestingTokenObject
    token: str
    r"""The actual token. This value is meant to be passed in the `__clerk_testing_token` query parameter with requests to the Frontend API."""
    expires_at: int
    r"""Unix timestamp of the token's expiration time.

    """
    
