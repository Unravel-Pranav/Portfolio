from sqlalchemy.orm import Session
from app.models.achievement_model import Achievement

def get_achievement(db: Session, achievement_id: int):
    return db.query(Achievement).filter(Achievement.id == achievement_id).first()

def get_achievements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Achievement).offset(skip).limit(limit).all()

def create_achievement(db: Session, achievement: dict):
    db_achievement = Achievement(**achievement)
    db.add(db_achievement)
    db.commit()
    db.refresh(db_achievement)
    return db_achievement

def update_achievement(db: Session, achievement_id: int, updates: dict):
    db_achievement = get_achievement(db, achievement_id)
    if not db_achievement:
        return None
    for key, value in updates.items():
        setattr(db_achievement, key, value)
    db.commit()
    db.refresh(db_achievement)
    return db_achievement

def delete_achievement(db: Session, achievement_id: int):
    db_achievement = get_achievement(db, achievement_id)
    if not db_achievement:
        return None
    db.delete(db_achievement)
    db.commit()
    return db_achievement 