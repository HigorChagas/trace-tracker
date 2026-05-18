from fastapi import APIRouter, status
from fastapi.params import Depends

from database.database import get_async_session
from schemas.user import Register
from services.user import register_user

router = APIRouter()


@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def user_register(register: Register, session=Depends(get_async_session)):
    return await register_user(
        session, register.email, register.password, register.name
    )
