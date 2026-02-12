from fastapi import APIRouter
from app.schemas.profile import ProfileInfoResponse
router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/info", response_model=ProfileInfoResponse)
async def get_profile_info():
    return ProfileInfoResponse(
        name="Trevor Febias",
        location="The Nairobi Hospital",
        year=2003
    )
