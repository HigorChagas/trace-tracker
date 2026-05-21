from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.error_history import ErrorHistory
from models.known_error import KnownError
from services.ai import analyze_error


async def send_log(session: AsyncSession, log: str, user_id: int):
    last_line = log.splitlines()[-1]
    last_line_lower = last_line.lower()
    known_error = await get_known_error(session, last_line_lower)
    if not known_error:
        raise HTTPException(status_code=404, detail="Error not found in our database")
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


async def get_error_history(session: AsyncSession, user_id: int, page: int, limit: int):
    offset = (page - 1) * limit
    stmt = (
        select(ErrorHistory)
        .limit(limit)
        .offset(offset)
        .where(ErrorHistory.user_id == user_id)
    )
    result = await session.execute(stmt)
    return result.scalars().all()


async def delete_error_history(session: AsyncSession, error_id: int, id: int):
    await search_error_history(session, error_id, id)
    stmt = delete(ErrorHistory).where(ErrorHistory.id == error_id)
    await session.execute(stmt)
    await session.commit()
    return {"message": "Item deleted successfully"}


async def search_error_history(session: AsyncSession, error_id: int, id: int):
    stmt = select(ErrorHistory).where(ErrorHistory.id == error_id)
    result = await session.execute(stmt)
    full_result = result.scalars().one_or_none()

    if not full_result:
        raise HTTPException(status_code=404, detail="History entry not found")

    if full_result.user_id != id:
        raise HTTPException(
            status_code=403, detail="You don't have permission to access this entry"
        )
    return full_result
