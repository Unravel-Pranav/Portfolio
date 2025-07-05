from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.schemas.image_schema import ImageOut
from app.config.db_session import get_db
from app.service.image_service import handle_image_upload, handle_image_delete

router = APIRouter(tags=["Images"])

@router.post("/upload-image/", response_model=ImageOut)
def upload_image(
    file: UploadFile = File(...),
    category: str = Form(...),
    owner_id: int = Form(...),
    db: Session = Depends(get_db)
):
    return handle_image_upload(db, file, category, owner_id)

@router.delete("/delete-image/{image_id}", response_model=ImageOut)
def delete_image(image_id: int, db: Session = Depends(get_db)):
    deleted = handle_image_delete(db, image_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Image not found")
    return deleted
