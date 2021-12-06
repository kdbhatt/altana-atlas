from fastapi import APIRouter

from .endpoints import apps


router = APIRouter()
router.include_router(apps.router, prefix="/app", tags=["app"])
