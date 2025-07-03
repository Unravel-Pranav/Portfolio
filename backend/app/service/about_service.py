from app.repository.about_repo import AboutRepository
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.repository import about_repo
from app.schemas.about_schema import AboutCreate,AboutBase
from app.config.db_session import get_db
import json

class AboutService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.repo = AboutRepository(db)  # Create instance here

    async def get_about(self):
        about_data = self.repo.get_about()
        if not about_data:
            raise HTTPException(status_code=404, detail="About info not found.")
        return about_data

    async def create_about(self, about: AboutCreate):
        existing = self.repo.get_about()
        if existing:
            raise HTTPException(status_code=400, detail="About info already exists.")
        created = self.repo.create_about(about)
        if created and isinstance(created.tech_stack, str):
            created.tech_stack = json.loads(created.tech_stack)
        return created

    async def delete_about(self):
        existing = self.repo.get_about()
        if not existing:
            raise HTTPException(status_code=404, detail="No About entry found to delete.")
        return self.repo.delete_about()

    async def update_about(self, about: AboutCreate):
        existing = self.repo.get_about()
        if not existing:
            raise HTTPException(status_code=404, detail="No About entry found to update.")
        updated = self.repo.update_about(about)
        if updated and isinstance(updated.tech_stack, str):
            updated.tech_stack = json.loads(updated.tech_stack)
        return updated
