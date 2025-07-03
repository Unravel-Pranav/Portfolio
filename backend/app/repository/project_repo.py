import json
from sqlalchemy.orm import Session
from app.models import project_model
from app.schemas import projects_schema

class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project: projects_schema.ProjectCreate):
        db_project = project_model.Project(
            project_name=project.project_name,
            start_date=project.start_date,
            end_date=project.end_date,
            title=project.title,
            description=project.description,
            tech_stack=json.dumps(project.tech_stack),
            image_url=project.image_url
        )
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def get_project(self, project_id: int):
        project = self.db.query(project_model.Project).filter(project_model.Project.id == project_id).first()
        if project:
            project.tech_stack = json.loads(project.tech_stack)
        return project

    def get_all_projects(self):
        projects = self.db.query(project_model.Project).all()
        for project in projects:
            project.tech_stack = json.loads(project.tech_stack)
        return projects

    def update_project(self, project_id: int, project: projects_schema.ProjectCreate):
        db_project = self.db.query(project_model.Project).filter(project_model.Project.id == project_id).first()
        if not db_project:
            return None
        db_project.project_name = project.project_name
        db_project.start_date = project.start_date
        db_project.end_date = project.end_date
        db_project.title = project.title
        db_project.description = project.description
        db_project.tech_stack = json.dumps(project.tech_stack)
        db_project.image_url = project.image_url
        self.db.commit()
        self.db.refresh(db_project)
        db_project.tech_stack = json.loads(db_project.tech_stack)
        return db_project

    def delete_project(self, project_id: int):
        db_project = self.db.query(project_model.Project).filter(project_model.Project.id == project_id).first()
        if not db_project:
            return None
        self.db.delete(db_project)
        self.db.commit()
        return db_project 