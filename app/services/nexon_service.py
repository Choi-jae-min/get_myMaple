import os
import httpx
from fastapi import HTTPException

class NexonAPI:
    def __init__(self):
        self.api_key = os.getenv("NEXON_API_KEY")
        self.base_url = os.getenv("NEXON_BASE_URL")

        if not self.api_key:
            raise RuntimeError("NEXON_API_KEY is not configured")

        if not self.base_url:
            raise RuntimeError("NEXON_BASE_URL is not configured")

    async def get(self, path: str, params: dict | None = None):
        url = f"{self.base_url}{path}"

        async with httpx.AsyncClient() as client:
            res = await client.get(
                url,
                params=params,
                headers={"x-nxopen-api-key": self.api_key},
            )

        if res.is_error:
            raise HTTPException(status_code=res.status_code, detail=res.text)

        return res.json()
