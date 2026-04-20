from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/check")
async def auth_check():
    return {"status": "auth working"}