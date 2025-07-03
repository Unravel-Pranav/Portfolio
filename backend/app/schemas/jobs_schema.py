from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class JobBase(BaseModel):
    company_name: str
    project_title: str
    start_date: date
    end_date: date
    description: str
    tech_stack: List[str]
    image_url: Optional[str]

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int

    class Config:
        orm_mode = True
