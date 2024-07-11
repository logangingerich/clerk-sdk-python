"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel
from enum import Enum
from typing import TypedDict


class TotalCountObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    TOTAL_COUNT = "total_count"


class TotalCountTypedDict(TypedDict):
    object: TotalCountObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    total_count: int
    

class TotalCount(BaseModel):
    object: TotalCountObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    total_count: int
    
