from fastapi import APIRouter

from app.address_book.views import addresses_router

router = APIRouter()

router.include_router(addresses_router, tags=["Address"], prefix="/address")
