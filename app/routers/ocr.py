from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import PlainTextResponse
import io
from manga_ocr import MangaOcr
import PIL.Image

router = APIRouter()
mocr = MangaOcr()


@router.post(
    "",
    summary="Extract Japanese Text from Manga Images",
    description=(
        "This endpoint receives an image file of a manga in Japanese and returns the extracted text in plain text. "
        "Supported image formats include JPEG and PNG, BMP, TIFF, and WebP."
    ),
    response_description="The extracted text from the image.",
    response_class=PlainTextResponse,
)
async def ocr(
    file: UploadFile = File(..., description="The image file to be processed."),
):
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
