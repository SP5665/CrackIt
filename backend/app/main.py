from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.resumes import router as resumes_router
from app.models import User, Resume

app = FastAPI(
    title="CrackIt API",
    description="Adaptive AI Interview Preparation Platform",
    version="1.0.0"
)

app.include_router(users_router)
app.include_router(resumes_router)

@app.get("/")
def root():
    return {"message": "CrackIt API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}