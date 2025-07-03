from fastapi import APIRouter, Depends
from app.schemas.about_schema import AboutCreate, AboutResponse
from app.service.about_service import AboutService

router = APIRouter(prefix="/about", tags=["About"])


@router.get("/", response_model=AboutResponse)
async def get_about(about_service: AboutService = Depends()):
    return await about_service.get_about()

@router.post("/", response_model=AboutResponse)
async def create_about(about: AboutCreate, about_service: AboutService = Depends()):
    return await about_service.create_about(about)

@router.put("/", response_model=AboutResponse)
async def update_about(about: AboutCreate, about_service: AboutService = Depends()):
    return await about_service.update_about(about)

@router.delete("/", response_model=AboutResponse)
async def delete_about(about_service: AboutService = Depends()):
    return await about_service.delete_about()
