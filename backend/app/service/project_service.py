from app.repository.project_repo import ProjectRepository
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.projects_schema import ProjectCreate
from app.config.db_session import get_db
import json

class ProjectService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.repo = ProjectRepository(db)

    async def get_project(self, project_id: int):
        project = self.repo.get_project(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found.")
        return project

    async def get_all_projects(self):
        return self.repo.get_all_projects()

    async def create_project(self, project: ProjectCreate):
        created = self.repo.create_project(project)
        if created and isinstance(created.tech_stack, str):
            created.tech_stack = json.loads(created.tech_stack)
        return created

    async def update_project(self, project_id: int, project: ProjectCreate):
        updated = self.repo.update_project(project_id, project)
        if not updated:
            raise HTTPException(status_code=404, detail="Project not found.")
        return updated

    async def delete_project(self, project_id: int):
        deleted = self.repo.delete_project(project_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Project not found.")
        return deleted 