from fastapi import APIRouter, status
from fastapi.param_functions import Depends

from database.database import get_async_session
from schemas.log import Message
from services.auth import get_current_user
from services.log import (
    delete_error_history,
    get_error_history,
    search_error_history,
    send_log,
)

router = APIRouter()


@router.post("/search-log/", status_code=status.HTTP_200_OK)
async def search_log(
    message: Message,
    current_user=Depends(get_current_user),
    session=Depends(get_async_session),
):
    return await send_log(session, message.log, current_user.id)


@router.get("/history/", status_code=status.HTTP_200_OK)
async def get_log_history(
    current_user=Depends(get_current_user),
    session=Depends(get_async_session),
    page: int = 1,
    limit: int = 10,
):
    return await get_error_history(session, current_user.id, page, limit)


@router.delete("/history/{error_id}", status_code=status.HTTP_200_OK)
async def delete_log_history(
    error_id: int,
    current_user=Depends(get_current_user),
    session=Depends(get_async_session),
):
    return await delete_error_history(session, error_id, current_user.id)


@router.get("/history/{error_id}", status_code=status.HTTP_200_OK)
async def get_log_history_by_id(
    error_id: int,
    current_user=Depends(get_current_user),
    session=Depends(get_async_session),
):
    return await search_error_history(session, error_id, current_user.id)
