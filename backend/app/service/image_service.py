from fastapi import UploadFile
from app.config.apwrite_config import storage, APPWRITE_BUCKET_ID
from app.repository.image_repo import save_image_url, delete_image_by_id
from appwrite.input_file import InputFile
import uuid
import io

def handle_image_upload(db, file: UploadFile):
    try:
        unique_id = str(uuid.uuid4())

        # Read file content
        file_content = file.file.read()
        
        # Convert UploadFile to Appwrite-compatible InputFile
        input_file = InputFile.from_bytes(file_content, filename=file.filename)

        # Upload to Appwrite Storage
        uploaded_file = storage.create_file(
            bucket_id=APPWRITE_BUCKET_ID,
            file_id=unique_id,
            file=input_file,
        )

        # Construct public image URL (adjust if needed for your region/endpoint)
        image_url = f"https://cloud.appwrite.io/v1/storage/buckets/6868fba60016c28b868f/files/{uploaded_file['$id']}/preview"

        # Save URL and file ID to your DB
        return save_image_url(db, image_url, uploaded_file['$id'])

    except Exception as e:
        print("Upload Error:", str(e))
        raise

def handle_image_delete(db, image_id: int):
    try:
        image = delete_image_by_id(db, image_id)
        if image:
            # Delete from Appwrite
            storage.delete_file(
                bucket_id=APPWRITE_BUCKET_ID,
                file_id=image.file_id
            )
        return image
    except Exception as e:
        print("Delete Error:", str(e))
        raise
