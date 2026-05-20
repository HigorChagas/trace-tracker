from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.error_history import ErrorHistory
from models.known_error import KnownError
from services.ai import analyze_error


async def send_log(session: AsyncSession, log: str, user_id: int):
    last_line = log.splitlines()[-1].lower()
    known_error = await get_known_error(session, last_line)
    if not known_error:
        raise HTTPException(status_code=404, detail="Error not found")
    ia_response = analyze_error(log)
    await save_error_history(session, last_line, log, ia_response, "Python", user_id)
    return ia_response


async def get_known_error(session: AsyncSession, log: str):
    stmt = select(KnownError).where(KnownError.error_name.ilike(f"%{log}%"))
    result = await session.execute(stmt)
    return result.scalars().one_or_none()


async def save_error_history(
    session: AsyncSession,
    error_name: str,
    context: str,
    ia_response: str,
    language: str,
    user_id: int,
):
    save_history = ErrorHistory(
        user_id=user_id,
        error_name=error_name,
        ia_response=ia_response,
        context=context,
        language=language,
    )

    session.add(save_history)
    await session.commit()
    return {"message": "Error registered!"}


async def get_error_history(session: AsyncSession, user_id: int):
    stmt = select(ErrorHistory).where(ErrorHistory.user_id == user_id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def delete_error_history(session: AsyncSession, error_id: int):
    stmt = delete(ErrorHistory).where(ErrorHistory.id == error_id)
    await session.execute(stmt)
    await session.commit()
    return {"message": "Item deleted successfully"}


async def search_error_history(session: AsyncSession, error_id: int):
    stmt = select(ErrorHistory).where(ErrorHistory.id == error_id)
    result = await session.execute(stmt)
    return result.scalars().one_or_none()
