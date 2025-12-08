from fastapi import APIRouter, HTTPException
import httpx
import os

router = APIRouter()

@router.get("/maple/characters")
async def get_maple_characters():
    api_key = os.getenv("NEXON_API_KEY")

    if not api_key:
        raise HTTPException(status_code=500, detail="NEXON_API_KEY is not configured")

    async with httpx.AsyncClient() as client:
        res = await client.get(
            "https://open.api.nexon.com/maplestory/v1/character/list",
            headers={"x-nxopen-api-key": api_key}
        )
        return res.json()
