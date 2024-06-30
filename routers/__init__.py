from aiogram import Router

from .user_router import router as user_router

routers: Router = Router()

routers.include_router(user_router)