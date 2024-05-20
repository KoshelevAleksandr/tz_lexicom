from fastapi import APIRouter, Depends, HTTPException

from api.schemas import CheckDataResponse, WriteData
from db.session import get_redis

data_router = APIRouter()


@data_router.post("/Write_data")
async def create_phone(body: WriteData, db = Depends(get_redis))
    try:
        return await _create_new_phone(body, db)
    except Exception as err:
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


@data_router.get("/Check_data", response_model=CheckDataResponse)
async def get_address_by_phone(phone: str, db = Depends(get_redis))
    address = await _get_address_by_phone(phone, db)
    if address is None:
        raise HTTPException(status_code=404, detail=f"Phone {phone} not found")
    return address
