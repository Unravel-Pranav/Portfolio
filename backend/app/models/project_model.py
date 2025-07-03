from sqlalchemy import Column, Integer, String, Date
from app.config.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    tech_stack = Column(String, nullable=False)
    image_url = Column(String)
