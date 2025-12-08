from fastapi import APIRouter
from typing import Optional

from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/characters")
async def get_maple_characters():
    return await nexon.get("/maplestory/v1/character/list")


@router.get("/maple/character/id/{name}",tags=["character"])
async def get_character_id(name: str):
    return await nexon.get(
        "/maplestory/v1/id",
        params={"character_name": name}
    )

@router.get("/maple/character/{id}",tags=["character"])
async def get_character_basic(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/basic", params=params)

@router.get("/maple/character/popularity/{id}",tags=["character"])
async def get_character_popularity(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/popularity", params=params)


@router.get("/maple/character/stat/{id}",tags=["character"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/stat", params=params)

@router.get("/maple/character/hyper-stat/{id}",tags=["character"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/hyper-stat", params=params)

@router.get("/maple/character/propensity/{id}",tags=["character"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/propensity", params=params)

@router.get("/maple/character/ability/{id}",tags=["character"])
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/ability", params=params)
