from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    file_id = Column(String, nullable=True)
    category = Column(String, nullable=False)  # e.g., 'achievement', 'about', etc.
    owner_id = Column(Integer, nullable=False) # the id of the resource it belongs to

