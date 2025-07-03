
from pydantic import BaseModel
from typing import Optional

class AchievementBase(BaseModel):
    title: str
    description: str
    link: Optional[str]
    image_url: Optional[str]

class AchievementCreate(AchievementBase):
    pass

class AchievementResponse(AchievementBase):
    id: int

    class Config:
        orm_mode = True
