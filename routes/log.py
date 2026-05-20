from fastapi import APIRouter, status
from fastapi.param_functions import Depends

from database.database import get_async_session
from schemas.log import Message
from services.auth import get_current_user
from services.log import send_log

router = APIRouter()


# TODO: adicionar get_current_user como Depends na rota /search-log/
@router.post("/search-log/", status_code=status.HTTP_200_OK)
async def search_log(
    message: Message,
    current_user=Depends(get_current_user),
    session=Depends(get_async_session),
):
    return await send_log(session, message.log, current_user.id)
