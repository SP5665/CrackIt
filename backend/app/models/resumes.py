from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func

from app.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    file_name = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)

    parsed_data = Column(JSON, nullable=True)

    uploaded_at = Column(
        DateTime,
        server_default=func.now()
    )