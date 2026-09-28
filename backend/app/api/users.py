from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.users import User
from app.schemas.users import UserCreate

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user