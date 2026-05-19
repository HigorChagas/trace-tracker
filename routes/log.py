from fastapi import APIRouter
from fastapi.param_functions import Depends

from schemas.log import Message
from services.auth import get_current_user
from services.log import send_log

router = APIRouter()


# TODO: adicionar get_current_user como Depends na rota /search-log/
@router.post("/search-log/")
async def search_log(message: Message, current_user=Depends(get_current_user)):
    return await send_log(message.log)
