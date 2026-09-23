from fastapi import FastAPI

app = FastAPI(
    title="CrackIt API",
    description="Adaptive AI Interview Preparation Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "CrackIt API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}