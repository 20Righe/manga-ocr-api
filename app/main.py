from fastapi import FastAPI
from app.routers import ocr

app = FastAPI()


app.include_router(ocr.router, prefix="/api/v1/ocr", tags=["OCR"])
