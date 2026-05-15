from fastapi import APIRouter

from schemas.log import Message
from services.log import send_log

router = APIRouter()


@router.post("/search-log/")
async def search_log(message: Message):
    return await send_log(message.log)
