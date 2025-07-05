from pydantic import BaseModel
from typing import Optional

class ImageCreate(BaseModel):
    url: str
    file_id: Optional[str] = None
    category: str
    owner_id: int

class ImageOut(ImageCreate):
    id: int

    class Config:
        orm_mode = True
