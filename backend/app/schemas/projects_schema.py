from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ProjectBase(BaseModel):
    project_name: str
    start_date: date
    end_date: date
    title: str
    description: str
    tech_stack: List[str]
    image_url: Optional[str]

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True
