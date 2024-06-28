from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.post("/", response_class=PlainTextResponse)
async def ocr():
    return "こんにちは、ORC"
