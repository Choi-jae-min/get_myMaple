from fastapi import APIRouter, HTTPException
import httpx
import os
from urllib.parse import quote
from typing import Optional

router = APIRouter()

@router.get("/maple/characters")
async def get_maple_characters():
    api_key = os.getenv("NEXON_API_KEY")
    base_url = os.getenv("NEXON_BASE_URL")

    if not api_key:
        raise HTTPException(status_code=500, detail="NEXON_API_KEY is not configured")

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{base_url}/maplestory/v1/character/list",
            headers={"x-nxopen-api-key": api_key}
        )
        return res.json()


@router.get("/maple/character/id/{name}")
async def get_maple_character_id_by_name(name : str):
    api_key = os.getenv("NEXON_API_KEY")
    base_url = os.getenv("NEXON_BASE_URL")

    if not api_key:
        raise HTTPException(status_code=500, detail="NEXON_API_KEY is not configured")

    encoded_name = quote(name)

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{base_url}/maplestory/v1/id?character_name={encoded_name}",
            headers={"x-nxopen-api-key": api_key}
        )
        return res.json()

@router.get("/maple/character/{id}")
async def get_maple_character_by_id(id: str, date: Optional[str] = None):
    api_key = os.getenv("NEXON_API_KEY")
    base_url = os.getenv("NEXON_BASE_URL")

    if not api_key:
        raise HTTPException(status_code=500, detail="NEXON_API_KEY is not configured")

    params = {"ocid": id}
    if date:
        params["date"] = date

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{base_url}/maplestory/v1/character/basic",
            params=params,
            headers={"x-nxopen-api-key": api_key}
        )

    return res.json()

@router.get("/maple/character/popularity/{id}")
async def get_maple_character_popularity_by_id(id: str, date: Optional[str] = None):
    api_key = os.getenv("NEXON_API_KEY")
    base_url = os.getenv("NEXON_BASE_URL")

    if not api_key:
        raise HTTPException(status_code=500, detail="NEXON_API_KEY is not configured")

    params = {"ocid": id}
    if date:
        params["date"] = date

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{base_url}/maplestory/v1/character/popularity",
            params=params,
            headers={"x-nxopen-api-key": api_key}
        )

    return res.json()

@router.get("/maple/character/stat/{id}")
async def get_maple_character_stat_by_id(id: str, date: Optional[str] = None):
    api_key = os.getenv("NEXON_API_KEY")
    base_url = os.getenv("NEXON_BASE_URL")

    if not api_key:
        raise HTTPException(status_code=500, detail="NEXON_API_KEY is not configured")

    params = {"ocid": id}
    if date:
        params["date"] = date

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{base_url}/maplestory/v1/character/stat",
            params=params,
            headers={"x-nxopen-api-key": api_key}
        )

    return res.json()
