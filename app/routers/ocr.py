from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import PlainTextResponse
import io
from manga_ocr import MangaOcr
import PIL.Image

router = APIRouter()
mocr = MangaOcr()


@router.post("", response_class=PlainTextResponse)
async def ocr(file: UploadFile = File(...)):
    allowed_content_types = [
        "image/jpeg",
        "image/png",
        "image/bmp",
        "image/tiff",
        "image/webp",
    ]

    if file.content_type not in allowed_content_types:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only JPEG, PNG, BMP, TIFF, and WebP are supported.",
        )
    try:
        img = PIL.Image.open(io.BytesIO(await file.read()))
        text = mocr(img)
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
