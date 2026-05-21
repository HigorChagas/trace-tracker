from fastapi import HTTPException
from pydantic.types import SecretStr
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from services.auth import (
    create_access_token,
    get_password_hash,
    get_user,
    verify_password,
)


async def register_user(
    session: AsyncSession, email: str, password: SecretStr, name: str
):
    hashed_password = get_password_hash(password.get_secret_value())
    user = User(email=email, name=name, password=hashed_password)
    get_user_email = await get_user(session, user.email)

    if get_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    session.add(user)

    await session.commit()
    return {"message": "User created successfully"}


async def login_user(session: AsyncSession, email: str, password: SecretStr):
    get_user_info = await get_user(session, email)

    if not get_user_info:
        raise HTTPException(status_code=404, detail="User not found")

    check_password = verify_password(
        password.get_secret_value(), get_user_info.password
    )

    if check_password:
        access_token = create_access_token({"sub": get_user_info.email})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")
