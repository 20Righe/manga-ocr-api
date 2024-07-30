from fastapi import FastAPI
from app.routers import ocr

app = FastAPI(
    title="Manga OCR API",
    description=(
        "Manga OCR API provides Optical Character Recognition (OCR) for Japanese manga images. "
        "This API wraps the `manga-ocr` library to extract text from manga images."
    ),
    version="0.1.0-beta",
    contact={
        "name": "20Righe",
        "url": "https://github.com/20Righe/manga-ocr-api",
    },
    license_info={
        "name": "Apache License",
        "url": "https://www.apache.org/licenses/",
    },
)


app.include_router(ocr.router, prefix="/api/v1/ocr", tags=["OCR"])
