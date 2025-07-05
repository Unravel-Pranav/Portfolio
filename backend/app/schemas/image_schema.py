from pydantic import BaseModel

class ImageOut(BaseModel):
    id: int
    image_url: str
    file_id: str

    class Config:
        from_attributes = True
