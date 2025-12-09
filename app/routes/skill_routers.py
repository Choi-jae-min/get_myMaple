from fastapi import APIRouter
from typing import Optional

from app.schemas.skill import SkillGrade
from app.services.nexon_service import NexonAPI

router = APIRouter()
nexon = NexonAPI()

@router.get("/maple/character/skill/{id}",
            tags=["Skill"])
async def get_character_skill(id: str,character_skill_grade : SkillGrade, date: Optional[str] = None):
    params = {"ocid": id , "character_skill_grade" : character_skill_grade.value}
    if date:
        params["date"] = date
    return await nexon.get("/maplestory/v1/character/skill", params=params)

