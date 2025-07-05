from sqlalchemy import Column, Integer, String
from app.config.database import Base

class ImageModel(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)
    file_id = Column(String, nullable=False) 

