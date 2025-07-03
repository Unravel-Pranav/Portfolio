from fastapi import FastAPI
from app.config.database import Base, engine
from app.controllers import about_controller, project_controller
from app.service.about_service import AboutService
from fastapi.routing import APIRouter

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(about_controller.router)
app.include_router(project_controller.router)
    

