from typing import Union

from api.schemas import CheckDataResponse, WriteData
from db.dals import DataDAL


async def _create_new_phone(body: WriteData, session):
    data_dal = DataDAL(session)
    return await data_dal.crete_phone(
        phone=body.phone,
        address=body.address,
    )


async def _get_address_by_phone(phone, session) -> Union[CheckDataResponse, None]:
    data_dal = DataDAL(session)
    address = await data_dal.get_address(
        phone=phone,
    )
    if address is not None:
        return address



async def _update_phone(body: WriteData, session):
    data_dal = DataDAL(session)
    return await data_dal.update_address(
        phone=body.phone,
        address=body.address,
    )