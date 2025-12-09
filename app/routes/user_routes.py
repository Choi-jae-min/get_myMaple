from fastapi import APIRouter, Query, Depends
from typing import Optional

from app.services.nexon_service import NexonAPI
from app.services.utility import validate_date_or_cursor

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/user/ouid",
            tags=["User"])
async def get_user_union():
    return await nexon.get("/maplestory/v1/ouid")


@router.get(
    "/maple/user/history/starforce",
    tags=["starforce"]
)
async def get_user_union(
        count: int = Query(
            ...,
            ge=10,
            lt=1000,
            description="10 이상 1000 미만"
        ),
        validated: dict = Depends(validate_date_or_cursor),
):
    params = {"count": count}

    if validated["date"]:
        params["date"] = validated["date"]
    if validated["cursor"]:
        params["cursor"] = validated["cursor"]

    return await nexon.get(
        "/maplestory/v1/history/starforce",
        params=params
    )

@router.get(
    "/maple/user/history/potential",
    tags=["starforce"]
)
async def get_user_union(
        count: int = Query(
            ...,
            ge=10,
            lt=1000,
            description="10 이상 1000 미만"
        ),
        validated: dict = Depends(validate_date_or_cursor),
):
    params = {"count": count}

    if validated["date"]:
        params["date"] = validated["date"]
    if validated["cursor"]:
        params["cursor"] = validated["cursor"]

    return await nexon.get(
        "/maplestory/v1/history/potential",
        params=params
    )

@router.get(
    "/maple/user/history/cube",
    tags=["starforce"]
)
async def get_user_union(
        count: int = Query(
            ...,
            ge=10,
            lt=1000,
            description="10 이상 1000 미만"
        ),
        validated: dict = Depends(validate_date_or_cursor),
):
    params = {"count": count}

    if validated["date"]:
        params["date"] = validated["date"]
    if validated["cursor"]:
        params["cursor"] = validated["cursor"]

    return await nexon.get(
        "/maplestory/v1/history/cube",
        params=params
    )