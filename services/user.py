from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from services.auth import get_password_hash, get_user


async def register_user(session: AsyncSession, email: str, password: str, name: str):
    hashed_password = get_password_hash(password)
    user = User(email=email, name=name, password=hashed_password)
    get_user_email = await get_user(session, user.email)

    if get_user_email:
        raise HTTPException(status_code=400, detail="User already registered")

    session.add(user)

    await session.commit()
    return {"message": "User created successfully"}

# async def login_user(session: AsyncSession, email: str, passowrd: str):
    
