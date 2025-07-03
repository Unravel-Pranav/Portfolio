import json
from sqlalchemy.orm import Session
from app.models import about_model
from app.schemas import about_schema


class AboutRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def create_about(self, about: about_schema.AboutCreate):
        db_about = about_model.About(
            name=about.name,
            description=about.description,
            tech_stack=json.dumps(about.tech_stack),  # Serialize list
            image_url=about.image_url
        )
        self.db.add(db_about)
        self.db.commit()
        self.db.refresh(db_about)
        return db_about

    def get_about(self):
        about = self.db.query(about_model.About).first()
        if about:
            about.tech_stack = json.loads(about.tech_stack)  # Deserialize back to list
        return about
    
    def update_about(self, about: about_schema.AboutCreate):
        db_about = self.db.query(about_model.About).first()
        db_about.name = about.name
        db_about.description = about.description
        db_about.tech_stack = json.dumps(about.tech_stack)  # Serialize list
        db_about.image_url = about.image_url
        self.db.commit()
        self.db.refresh(db_about)
        return db_about

    def delete_about(self):
        about = self.db.query(about_model.About).first()
        self.db.delete(about)
        self.db.commit()
        return about
