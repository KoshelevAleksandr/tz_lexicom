import uuid
import re

from fastapi import HTTPException
from pydantic import BaseModel, ConfigDict, field_validator

LETTER_MATCH_PATTERN = re.compile(r"^[0-9]")


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class CheckDataResponse(TunedModel):
    phone: str
    address: str


class WriteData(BaseModel):
    phone: str
    address: str

    @field_validator("phone")
    def validate_phone(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Phone should contains only digit"
            )
        return value


class WriteDataResponse(TunedModel):
    status: bool
    phone: str
    address: str
