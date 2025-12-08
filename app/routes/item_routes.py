from fastapi import APIRouter
from typing import Optional

from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/character/item-equipment/{id}")
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/item-equipment", params=params)

@router.get("/maple/character/cashitem-equipment/{id}")
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/cashitem-equipment", params=params)

