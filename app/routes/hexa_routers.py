from fastapi import APIRouter
from typing import Optional

from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/character/hexamatrix/{id}",
            tags=["Hexamatrix"])
async def get_character_hexamatrix(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date
    return await nexon.get("/maplestory/v1/character/hexamatrix", params=params)


@router.get("/maple/character/hexamatrix-state/{id}",
            tags=["Hexamatrix"])
async def get_character_hexamatrix_state(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date
    return await nexon.get("/maplestory/v1/character/hexamatrix-state", params=params)
