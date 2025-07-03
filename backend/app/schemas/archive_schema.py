from pydantic import BaseModel
from typing import Optional

class ArchiveBase(BaseModel):
    year: int
    title: str
    made_at: str
    built_with: str
    link: Optional[str]

class ArchiveCreate(ArchiveBase):
    pass

class ArchiveResponse(ArchiveBase):
    id: int

    class Config:
        orm_mode = True
