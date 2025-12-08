from fastapi import APIRouter, HTTPException
import httpx
import os
from urllib.parse import quote
from typing import Optional

from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/characters")
async def get_maple_characters():
    return await nexon.get("/maplestory/v1/character/list")


@router.get("/maple/character/id/{name}")
async def get_character_id(name: str):
    return await nexon.get(
        "/maplestory/v1/id",
        params={"character_name": name}
    )

@router.get("/maple/character/{id}")
async def get_character_basic(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/basic", params=params)

@router.get("/maple/character/popularity/{id}")
async def get_character_popularity(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/popularity", params=params)


@router.get("/maple/character/stat/{id}")
async def get_character_stat(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/character/stat", params=params)
