from fastapi import APIRouter, Depends, Path
from app.schemas.projects_schema import ProjectCreate, ProjectResponse
from app.service.project_service import ProjectService
from typing import List

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=List[ProjectResponse])
async def get_all_projects(service: ProjectService = Depends()):
    return await service.get_all_projects()

@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: int = Path(...), service: ProjectService = Depends()):
    return await service.get_project(project_id)

@router.post("/", response_model=ProjectResponse)
async def create_project(project: ProjectCreate, service: ProjectService = Depends()):
    return await service.create_project(project)

@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: int, project: ProjectCreate, service: ProjectService = Depends()):
    return await service.update_project(project_id, project)

@router.delete("/{project_id}", response_model=ProjectResponse)
async def delete_project(project_id: int, service: ProjectService = Depends()):
    return await service.delete_project(project_id) 