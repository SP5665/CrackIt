from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, UploadFile, File

from app.database import get_db
from app.models.resumes import Resume

router = APIRouter(
    prefix="/api/resumes",
    tags=["Resumes"]
)


@router.get("/")
def get_resumes(db: Session = Depends(get_db)):
    resumes = db.query(Resume).all()
    return resumes

@router.post("/upload")
def upload_resume(file: UploadFile = File(...)):

    allowed_types = [
        "application/pdf"
    ]

    if file.content_type not in allowed_types:
        return {
            "error": "Only PDF files are allowed"
        }

    return {
        "file_name": file.filename,
        "file_type": file.content_type,
        "message": "File type is valid"
    }