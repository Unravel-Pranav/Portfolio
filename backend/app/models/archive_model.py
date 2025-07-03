from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Archive(Base):
    __tablename__ = "archives"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    made_at = Column(String, nullable=False)
    built_with = Column(String, nullable=False)
    link = Column(String)
