from fastapi import Query, HTTPException, Depends
from typing import Optional

def validate_date_or_cursor(
        date: Optional[str] = Query(
            None,
            regex=r"^\d{4}-\d{2}-\d{2}$",
            description="YYYY-MM-DD 형식"
        ),
        cursor: Optional[str] = Query(
            None,
            description="Cursor 값"
        ),
):
    if not date and not cursor:
        raise HTTPException(
            status_code=400,
            detail="date 또는 cursor 중 하나는 반드시 필요합니다."
        )

    return {"date": date, "cursor": cursor}
