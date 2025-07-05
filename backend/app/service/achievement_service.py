from app.repository.achievement_repo import (
    create_achievement, get_achievement, get_achievements, update_achievement, delete_achievement
)

def handle_achievement_create(db, data: dict):
    # image_url is just a string in data, no upload
    return create_achievement(db, data)

def handle_achievement_update(db, achievement_id: int, updates: dict):
    # image_url is just a string in updates, no upload
    return update_achievement(db, achievement_id, updates)

def handle_achievement_delete(db, achievement_id: int):
    return delete_achievement(db, achievement_id)

def handle_get_achievement(db, achievement_id: int):
    return get_achievement(db, achievement_id)

def handle_get_achievements(db, skip: int = 0, limit: int = 100):
    return get_achievements(db, skip, limit) 