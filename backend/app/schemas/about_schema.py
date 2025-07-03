from typing import List
from pydantic import BaseModel

class AboutBase(BaseModel):
    name: str
    description: str
    tech_stack: List[str]
    image_url: str

class AboutCreate(AboutBase):
    pass

class AboutResponse(AboutBase):
    id: int

    class Config:
        orm_mode = True
