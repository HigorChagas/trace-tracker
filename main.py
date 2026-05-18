from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database import init_db
from routes.log import router as log_router
from routes.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(log_router)
app.include_router(user_router)
