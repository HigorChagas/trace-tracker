from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.known_error import KnownError
from services.ai import analyze_error


async def send_log(session: AsyncSession, log: str):
    last_line = log.splitlines()[-1].lower()
    known_error = await get_known_error(session, last_line)
    if not known_error:
        raise HTTPException(status_code=404, detail="Error not found")
    return analyze_error(log)


async def get_known_error(session: AsyncSession, log: str):
    stmt = select(KnownError).where(KnownError.error_name.ilike(f"%{log}%"))
    result = await session.execute(stmt)
    return result.scalars().one_or_none()
