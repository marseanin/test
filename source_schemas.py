from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, Json, UUID4, Strict, field_validator
import json
from src.product.schemas import Product


class SourceBase(BaseModel):
    account_id: int | None = Field(None, alias="account_id")
    setting: Json | None = Field(None, alias="setting")
    name: str | None = Field(None, alias="name")


class Source(SourceBase):
    """User Models Schema"""

    model_config = ConfigDict(from_attributes=True, allow_extra=True)
    id: int | None = Field(None, alias="id")
    source_id: UUID4 | None = Field(None, alias="source_id")
    private_key: UUID4 | None = Field(None, alias="private_key")
    access_token_id: int | None = Field(None, alias="access_token_id")
    status: str | None = Field("active", alias="status")
    product: Product | None = None
    is_active: bool | None = Field(True, alias="is_active")

    @field_validator("setting", mode="before", check_fields=False)
    @classmethod
    def dict_to_str(cls, value: dict):
        return json.dumps(value)


class SourceCreate(SourceBase):
    """Customer Models Schema for Update"""

    product_id: int | None = Field(None, alias="product_id")
    # setting: Json | None = Field(None, alias="setting")
    pass


class SourceUpdate(SourceBase):
    """Customer Models Schema for Update"""

    pass


class SourcePartialUpdate(SourceBase):
    """Customer Models Schema for Update"""

    pass
