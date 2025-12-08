from fastapi import APIRouter
from typing import Optional

from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/character/item-equipment/{id}",
            tags=["Equipment"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/item-equipment", params=params)

@router.get("/maple/character/cashitem-equipment/{id}",
            tags=["Equipment"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/cashitem-equipment", params=params)

@router.get("/maple/character/symbol-equipment/{id}",
            tags=["Equipment"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/symbol-equipment", params=params)


@router.get("/maple/character/set-effect/{id}",tags=["Equipment"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/set-effect", params=params)
