from fastapi import APIRouter, status
from fastapi.params import Depends

from database.database import get_async_session
from schemas.user import Login, Register
from services.user import login_user, register_user

router = APIRouter()


@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def user_register(register: Register, session=Depends(get_async_session)):
    return await register_user(
        session, register.email, register.password, register.name
    )


@router.post("/login/", status_code=status.HTTP_200_OK)
async def user_login(login: Login, session=Depends(get_async_session)):
    return await login_user(session, login.email, login.password)
