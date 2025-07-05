from sqlalchemy.orm import Session
from app.models.image_model import ImageModel

def save_image_url(db: Session, image_url: str, file_id: str) -> ImageModel:
    image = ImageModel(image_url=image_url, file_id=file_id)
    db.add(image)
    db.commit()
    db.refresh(image)
    return image

def delete_image_by_id(db: Session, image_id: int) -> ImageModel:
    image = db.query(ImageModel).filter(ImageModel.id == image_id).first()
    if image:
        db.delete(image)
        db.commit()
    return image
