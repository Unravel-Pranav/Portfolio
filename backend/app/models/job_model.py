from sqlalchemy import Column, Integer, String, Date
from app.config.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    project_title = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    tech_stack = Column(String, nullable=False)
    image_url = Column(String)
