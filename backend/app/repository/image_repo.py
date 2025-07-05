from sqlalchemy.orm import Session
from app.models.image_model import Image

def save_image_url(db: Session, url, file_id, category, owner_id):
    db_image = Image(url=url, file_id=file_id, category=category, owner_id=owner_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_images_by_category_and_owner(db: Session, category: str, owner_id: int):
    return db.query(Image).filter_by(category=category, owner_id=owner_id).all()

def get_image(db: Session, image_id: int):
    return db.query(Image).filter(Image.id == image_id).first()

def delete_image_by_id(db: Session, image_id: int):
    db_image = get_image(db, image_id)
    if db_image:
        db.delete(db_image)
        db.commit()
    return db_image
