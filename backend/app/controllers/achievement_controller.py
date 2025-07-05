from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.achievements_schema import AchievementCreate, AchievementResponse
from app.config.db_session import get_db
from app.service.achievement_service import (
    handle_achievement_create, handle_achievement_update, handle_achievement_delete,
    handle_get_achievement, handle_get_achievements
)
from typing import List

router = APIRouter(tags=["Achievements"])

@router.post("/achievements/", response_model=AchievementResponse)
def create_achievement(
    data: AchievementCreate,
    db: Session = Depends(get_db)
):
    return handle_achievement_create(db, data.dict())

@router.get("/achievements/", response_model=List[AchievementResponse])
def list_achievements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return handle_get_achievements(db, skip, limit)

@router.get("/achievements/{achievement_id}", response_model=AchievementResponse)
def get_achievement(achievement_id: int, db: Session = Depends(get_db)):
    achievement = handle_get_achievement(db, achievement_id)
    if not achievement:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return achievement

@router.put("/achievements/{achievement_id}", response_model=AchievementResponse)
def update_achievement(
    achievement_id: int,
    updates: AchievementCreate,
    db: Session = Depends(get_db)
):
    achievement = handle_achievement_update(db, achievement_id, updates.dict())
    if not achievement:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return achievement

@router.delete("/achievements/{achievement_id}", response_model=AchievementResponse)
def delete_achievement(achievement_id: int, db: Session = Depends(get_db)):
    achievement = handle_achievement_delete(db, achievement_id)
    if not achievement:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return achievement 