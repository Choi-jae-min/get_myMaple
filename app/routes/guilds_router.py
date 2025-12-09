from fastapi import APIRouter
from typing import Optional

from app.schemas.world_name import WorldName
from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/guild",
            tags=["guild"])
async def get_character_hexamatrix(guild_name: str, world_name: WorldName):
    params = {"guild_name": guild_name, "world_name" : world_name.value}

    return await nexon.get("/maplestory/v1/guild/id", params=params)

@router.get("/maple/guild/{id}",
            tags=["guild"])
async def get_character_hexamatrix(id: str, date: Optional[str] = None):
    params = {"oguild_id": id}
    if date:
        params["date"] = date

    return await nexon.get("/maplestory/v1/guild/basic", params=params)

