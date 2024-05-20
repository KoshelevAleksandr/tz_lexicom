import uuid

from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class CheckDataResponse(TunedModel):
    address: str


class WriteData(BaseModel):
    phone: str
    address: str
