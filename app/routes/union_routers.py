from fastapi import APIRouter
from typing import Optional

from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/user/union/{id}",
            tags=["union"])
async def get_user_union(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date
    return await nexon.get("/maplestory/v1/user/union", params=params)


@router.get("/maple/user/union-raider/{id}",
            tags=["union"])
async def get_user_union_raider(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date
    return await nexon.get("/maplestory/v1/user/union-raider", params=params)


@router.get("/maple/user/union-artifact/{id}",
            tags=["union"])
async def get_user_union_artifact(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date
    return await nexon.get("/maplestory/v1/user/union-artifact", params=params)


@router.get("/maple/user/union-champion/{id}",
            tags=["union"])
async def get_user_union_champion(id: str, date: Optional[str] = None):
    params = {"ocid": id}
    if date:
        params["date"] = date
    return await nexon.get("/maplestory/v1/user/union-champion", params=params)
