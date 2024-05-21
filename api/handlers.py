from fastapi import APIRouter, Depends, HTTPException

from api.actions.data_actions import _create_new_phone, _get_address_by_phone, _update_phone
from api.schemas import CheckDataResponse, WriteData, WriteDataResponse
from db.session import get_redis

data_router = APIRouter()


@data_router.post("/Write_data", response_model=WriteDataResponse)
async def create_phone(body: WriteData, db=Depends(get_redis)):
    try:
        address = await _get_address_by_phone(body.phone, db)
        if address is not None:
            raise HTTPException(status_code=404, detail=f"Phone {body.phone} already exists")
        status = await _create_new_phone(body, db)
        return WriteDataResponse(
            status=status,
            phone=body.phone,
            address=body.address
        )
    except Exception as err:
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


@data_router.get("/Check_data", response_model=CheckDataResponse)
async def get_address_by_phone(phone: str, db=Depends(get_redis)):
    address = await _get_address_by_phone(phone, db)
    if address is None:
        raise HTTPException(status_code=404, detail=f"Phone {phone} not found")
    return CheckDataResponse(phone=phone, address=address)


@data_router.put("/Write_data")
async def update_phone(body: WriteData, db=Depends(get_redis)):
    return body

    # try:
    #     updated = await _get_address_by_phone(body.phone, db)
    #     if updated is None:
    #         raise HTTPException(status_code=404, detail=f"Phone {body.phone} not found")
    #     return updated
    # except Exception as err:
    #     raise HTTPException(status_code=503, detail=f"Database error: {err}")

