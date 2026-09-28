from pydantic import BaseModel

class ResumeResponse(BaseModel):
    id: int
    user_id: int
    file_name: str
    file_type: str

    class Config:
        from_attributes = True